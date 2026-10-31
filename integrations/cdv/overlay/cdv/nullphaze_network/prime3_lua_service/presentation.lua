-- Read-only notifications; SendEvent never mutates inventory or receipts. Keep this callback
-- on the retail Lua thread and preserve the exact named event/bridge API used by its
-- matching source builder.
-- Read-only notifications; SendEvent never mutates inventory or receipts.
CP3WNetworkHUD = {elapsed = 0, applied = 0, rejects = 0, connected = false, checks = 0, error = 0}
local notice_names = {"PickupMissileReceived", "NetworkFailed", "NetworkDisconnected",
    "NetworkIPReady", "NetworkSocketReady", "NetworkHello", "NetworkReady", "NetworkRejected"}
local notice_count = 0
for index, name in ipairs(notice_names) do notice_count = notice_count + 1 end
for index = notice_count, 1, -1 do
    table.insert(CP3WProbe.notice_order, 1, notice_names[index])
end
local function notify(name)
    CP3WProbe.notices[name] = true
end
local function sample_network()
    if type(CP3WNetworkStatus) ~= "function" then return end
    local value = CP3WNetworkStatus()
    if type(value) ~= "string" or string.len(value) ~= 125 then return end
    local fields = {}
    for index = 1, 14 do
        local field = tonumber(string.sub(value, (index - 1) * 9 + 1, (index - 1) * 9 + 8), 16)
        if not field then return end
        fields[index] = field
    end
    local hud = CP3WNetworkHUD
    if hud.owner and (fields[13] ~= hud.owner or fields[14] ~= hud.generation) then
        CP3WProbe.notices.PickupMissileReceived = nil
    end
    hud.owner, hud.generation = fields[13], fields[14]
    local ip, phase, failure = fields[2], fields[3], fields[4]
    if ip ~= 0 and ip < 3758096384 and not hud.ip then
        hud.ip = ip
        local function octet(number)
            return number - math.floor(number / 256) * 256
        end
        hud.ip_address = string.format("%d.%d.%d.%d", math.floor(ip / 16777216),
            octet(math.floor(ip / 65536)), octet(math.floor(ip / 256)), octet(ip))
        notify("NetworkIPReady")
    end
    if phase >= 4 and phase ~= 9 and not hud.socket then
        hud.socket = true
        notify("NetworkSocketReady")
    end
    local connected = fields[5] == 1 and failure == 0
    if connected and not hud.connected then notify("NetworkHello") end
    if not connected and hud.connected then
        CP3WProbe.notices.NetworkHello = nil
        CP3WProbe.notices.NetworkReady = nil
        notify("NetworkDisconnected")
    end
    if connected and fields[6] == 3 and hud.checks ~= 3 then notify("NetworkReady") end
    if fields[8] > hud.rejects then notify("NetworkRejected") end
    if failure ~= 0 and failure ~= hud.error then notify("NetworkFailed") end
    -- Only an actual native application advances this counter. Loaded receipts
    -- and duplicate network replies do not play the pickup presentation.
    if fields[13] ~= 0 and fields[11] > hud.applied and fields[11] == fields[12] then
        notify("PickupMissileReceived")
    end
    hud.applied, hud.rejects, hud.connected, hud.checks, hud.error = fields[11], fields[8], connected, fields[6], failure
end
local original_think = OnThink
function OnThink(dt)
    original_think(dt)
    if type(dt) ~= "number" or dt ~= dt or dt <= 0 or dt > 1 then return end
    CP3WNetworkHUD.elapsed = CP3WNetworkHUD.elapsed + dt
    if CP3WNetworkHUD.elapsed < 0.5 then return end
    CP3WNetworkHUD.elapsed = 0
    sample_network()
end
