# Addon-local alignment correction for edited Corruption MREA sections. Boundary names here:
# next_instance_id, SeedMrea.
"""Addon-local alignment correction for edited Corruption MREA sections."""

from retro_data_structures.formats.mrea import Mrea, MREAConstruct
from retro_data_structures.formats.script_object import InstanceId


def next_instance_id(area, area_index):
    """Reserve generated objects and dormant links as well as ordinary layers."""
    actors = [actor for layer in [*area.script_layers, area.generated_objects_layer]
              for actor in layer.instances]
    reserved = {int(actor.id.without_layer) for actor in actors}
    reserved.update(int(link.target.without_layer) for actor in actors for link in actor.connections)
    highest = max((actor.id.instance for actor in actors), default=0)
    for instance in range(highest + 1, 65536):
        candidate = InstanceId.new(0, area_index, instance)
        if int(candidate) not in reserved:
            return candidate
    raise ValueError("No unused network script instance ID available")


class _AlignedConstruct(MREAConstruct):
    def _encode_compressed_blocks(self, data_sections, section_index, context, path):
        # RDS 0.44 pads each section while compressing but counts unpadded sizes.
        # Normalize the shared list so both block and section headers agree.
        for index, section in enumerate(data_sections):
            data_sections[index] = section + bytes(-len(section) % 32)
        return super()._encode_compressed_blocks(data_sections, section_index, context, path)


_CONSTRUCT = _AlignedConstruct()


class SeedMrea(Mrea):
    @classmethod
    def construct_class(cls, target_game):
        return _CONSTRUCT
