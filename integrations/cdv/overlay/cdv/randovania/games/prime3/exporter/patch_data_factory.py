# Translate the frontend's seed/preset state into this game's export fields. Keep recipient-
# aware pickup data, starting state and presentation fields separate at that boundary.
# Boundary names here: multiworld_model_name, CorruptionPatchDataFactory.
from __future__ import annotations

import randovania
from randovania.exporter.patch_data_factory import PatchDataFactory
from randovania.game.game_enum import RandovaniaGame
from randovania.game_description.resources.pickup_index import PickupIndex
from randovania.games.prime3.layout.corruption_configuration import CorruptionConfiguration
from randovania.games.prime3.layout.corruption_cosmetic_patches import CorruptionCosmeticPatches, CorruptionSuit
from randovania.games.prime3.patcher import gollop_corruption_patcher
from randovania.games.prime3.olympus import OLYMPUS_REGION, OLYMPUS_PICKUP_INDICES


def multiworld_model_name(location: dict) -> str:
    """Choose an available Corruption model without assigning its native grant."""
    name = location["item_name"]
    aliases = {"Morph Ball Bomb": "Morph Ball Bombs", "Bombs": "Morph Ball Bombs",
               "Ship Grapple Beam": "Ship Grapple", "Energy Cell": "Energy Cell 1"}
    name = aliases.get(name, name)
    if name in gollop_corruption_patcher.ITEM_NAME_TO_LETTER_MAPPING:
        return name
    # Other-game-only meshes are not shipped by Corruption. Preserve the explicit
    # placeholder for those until a separately validated model asset exists.
    return "Scan Visor"


class CorruptionPatchDataFactory(PatchDataFactory):
    configuration: CorruptionConfiguration
    cosmetic_patches: CorruptionCosmeticPatches

    def game_enum(self) -> RandovaniaGame:
        return RandovaniaGame.METROID_PRIME_CORRUPTION

    def create_game_specific_data(self) -> dict:
        cosmetic = self.cosmetic_patches
        assert isinstance(cosmetic, CorruptionCosmeticPatches)
        configuration = self.configuration
        assert isinstance(configuration, CorruptionConfiguration)
        # Nullphaze modification, 2026-10-16: reject excluded patches before
        # creating export data, including when importing an older .rdvgame.
        if configuration.MP3Update or configuration.disable_deflicker:
            raise ValueError("MP3Update and its deflicker patch are excluded from NullPhaaze.")
        patches = self.patches
        game = self.game
        if patches.starting_location.region == OLYMPUS_REGION:
            raise ValueError("G.F.S. Olympus cannot be a starting location. Generate a new seed.")
        for player, player_patches in self.description.all_patches.items():
            if self.description.get_preset(player).game != RandovaniaGame.METROID_PRIME_CORRUPTION:
                continue
            if any(index.index in OLYMPUS_PICKUP_INDICES and target.pickup.name != "Nothing"
                   for index, target in player_patches.pickup_assignment.items()):
                raise ValueError("This seed places items on G.F.S. Olympus. Generate a new seed.")
        multiworld = None
        if self.players_config.is_multiworld:
            from randovania.games.prime3.multiworld.manifest import create_manifest  # noqa: PLC0415

            multiworld = create_manifest(self)

        pickup_names = []
        for index in range(game.region_list.num_pickup_nodes):
            p_index = PickupIndex(index)
            if multiworld is not None:
                # This chooses visuals only. The GPL addon MUST neutralize the
                # core grant and replace its event behavior before publication.
                name = multiworld_model_name(multiworld["locations"][index])
            elif p_index in patches.pickup_assignment:
                name = patches.pickup_assignment[p_index].pickup.name
            else:
                name = "Missile Expansion"
            # Olympus is physically disabled by the core export flag. Keep the
            # original layout alphabet; Nothing uses a harmless visual placeholder.
            pickup_names.append("Scan Visor" if index in OLYMPUS_PICKUP_INDICES or name == "Nothing" else name)

        layout_string = gollop_corruption_patcher.layout_string_for_items(pickup_names)
        starting_location = patches.starting_location

        missile_required_mains = [
            ammo_state.requires_main_item
            for ammo_definition, ammo_state in self.configuration.ammo_pickup_configuration.pickups_state.items()
            if ammo_definition.name == "Missile Expansion"
        ][0]

        ship_missile_required_mains = [
            ammo_state.requires_main_item
            for ammo_definition, ammo_state in self.configuration.ammo_pickup_configuration.pickups_state.items()
            if ammo_definition.name == "Ship Missile Expansion"
        ][0]

        mp3_update = self.configuration.MP3Update
        disable_deflicker = self.configuration.disable_deflicker
        phaaze_skip = self.configuration.teleporters.skip_final_bosses

        starting_items = patches.starting_resources()
        starting_items.add_resource_gain(
            [
                (
                    game.resource_database.get_item_by_name("Suit Type"),
                    cosmetic.player_suit.value,
                ),
            ]
        )

        player_suit_value = self.cosmetic_patches.player_suit.value
        suit_type_tuple = [
            (resource, quantity)
            for resource, quantity in starting_items.as_resource_gain()
            if resource.long_name == "Suit Type"
        ]
        if len(suit_type_tuple) > 0:
            suit_type_resource, suit_type_quantity = suit_type_tuple[0]
            if suit_type_quantity > player_suit_value and suit_type_quantity < CorruptionSuit.CORRUPTED_50.value:
                starting_items.add_resource_gain(
                    [
                        (suit_type_resource, CorruptionSuit.CORRUPTED_50.value - suit_type_quantity + 1),
                    ]
                )

        ship_grapple_tuple = [
            (resource, quantity)
            for resource, quantity in starting_items.as_resource_gain()
            if resource.long_name == "Ship Grapple"
        ]
        if len(ship_grapple_tuple) > 0:
            _, ship_grapple_quantity = ship_grapple_tuple[0]
            if ship_grapple_quantity > 0 and not mp3_update:
                raise ValueError("Ship Grapple is not a possible starting item without MP3Update enabled.")

        if configuration.start_with_corrupted_hypermode:
            hypermode_original = 0
        else:
            hypermode_original = 1

        starting_items_text = gollop_corruption_patcher.starting_items_for(starting_items, hypermode_original)
        starting_location_text = gollop_corruption_patcher.starting_location_for(
            game, starting_location.area_identifier
        )
        commands = "\n".join(
            [
                f'set seed="{layout_string}"',
                f'set "starting_items={starting_items_text}"',
                f'set "starting_location={starting_location_text}"',
                f'set "random_door_colors={str(cosmetic.random_door_colors).lower()}"',
                f'set "random_welding_colors={str(cosmetic.random_welding_colors).lower()}"',
            ]
        )

        result = {
            "menu_identity": {
                "version": randovania.VERSION,
                "word_hash": self.description.shareable_word_hash,
                "seed_hash": self.description.shareable_hash,
            },
            "commands": commands,
            "seed": layout_string,
            "pickup_scan_text": [
                {"index": index, "item_name": patches.pickup_assignment[PickupIndex(index)].pickup.name
                 if PickupIndex(index) in patches.pickup_assignment else "Missile Expansion", "local": True}
                for index in range(game.region_list.num_pickup_nodes)
            ],
            "nothing_locations": sorted(index.index for index, target in patches.pickup_assignment.items()
                                        if target.pickup.name == "Nothing"),
            "exclude_olympus": True,
            "warp_to_space": configuration.warp_to_space,
            "fast_ziplines": configuration.fast_ziplines,
            "seed_hints": configuration.seed_hints,
            "starting_items": starting_items_text,
            "starting_location": starting_location_text,
            "random_door_colors": cosmetic.random_door_colors,
            "random_welding_colors": cosmetic.random_welding_colors,
            "missile_required_mains": missile_required_mains,
            "ship_missile_required_mains": ship_missile_required_mains,
            "phaaze_skip": phaaze_skip,
            "mp3_update": mp3_update,
            "disable_deflicker": disable_deflicker,
        }
        if multiworld is not None:
            result["multiworld"] = multiworld
            result["pickup_scan_text"] = [
                {key: row[key] for key in ("index", "item_name", "local", "recipient_name")}
                for row in multiworld["locations"]
            ]
            from randovania.games.prime3.exporter.models import model_plan

            result["multiworld_models"] = model_plan(multiworld)
        from randovania.games.prime3.exporter.item_location_hints import create_data as create_item_hints
        result['item_location_hints'] = create_item_hints(self)
        if configuration.seed_hints:
            from randovania.games.prime3.layout.hint_mode import LOCATION_HINT_FIELDS
            result['hint_settings'] = {
                field: getattr(configuration, field).value for field in LOCATION_HINT_FIELDS
            }
            result['hint_settings']['core_hint'] = configuration.core_hint.value
            from randovania.games.prime3.exporter.seed_hints import create_hint_data
            result["hint_data"] = create_hint_data(self)
            from randovania.games.prime3.exporter.hyper_hints import create_data as create_hyper_hints
            result["hyper_item_hints"] = create_hyper_hints(self)
        return result
