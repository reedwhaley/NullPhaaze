-- Called only from protected OnThink sampling on the retail Lua thread. Keep this callback
-- on the retail Lua thread and preserve the exact named event/bridge API used by its
-- matching source builder.
-- Called only from protected OnThink sampling on the retail Lua thread.
function CP3WReadLocationSnapshot()
    local text = CP3WReadLocation()
    if text == nil then return {available = false} end
    if type(text) ~= "string" or string.len(text) ~= 59
        or string.sub(text, 17, 17) ~= ":" or string.sub(text, 34, 34) ~= ":"
        or string.sub(text, 51, 51) ~= ":" then error("invalid location format") end
    local world = string.sub(text, 1, 16)
    local area = string.sub(text, 18, 33)
    local internal = string.sub(text, 35, 50)
    local index = string.sub(text, 52, 59)
    for _, value in ipairs({world, area, internal, index}) do
        if string.find(value, "[^0-9a-f]") then error("invalid location ID") end
    end
    index = tonumber(index, 16)
    if not index or index < 0 or index >= 512 then error("invalid location index") end
    return {available = true, world_id = world, area_id = area,
        internal_id = internal, area_index = index}
end

function CP3WPublishLocation(location)
    local old = CP3WProbe.location
    CP3WProbe.location = location
    if location.available then
        CP3WProbe.notices.ProbeLocationUnavailable = nil
        if not old.available then
            CP3WProbe.notices.ProbeLocationReady = true
        elseif old.world_id ~= location.world_id or old.area_id ~= location.area_id
            or old.area_index ~= location.area_index then
            CP3WProbe.location_changes = CP3WProbe.location_changes + 1
            CP3WProbe.notices.ProbeLocationChanged = true
        end
    else
        CP3WProbe.notices.ProbeLocationReady = nil
        CP3WProbe.notices.ProbeLocationChanged = nil
        if old.available then CP3WProbe.notices.ProbeLocationUnavailable = true end
    end
end
