-- Save-level network service. Only successful item applications may notify. Keep this
-- callback on the retail Lua thread and preserve the exact named event/bridge API used by
-- its matching source builder.
-- Save-level network service. Only successful item applications may notify.
local elapsed = 0
local applied = 0
function OnThink(dt)
    if type(dt) ~= "number" or dt ~= dt or dt <= 0 or dt > 1 then return end
    elapsed = elapsed + dt
    if elapsed < 0.5 then return end
    elapsed = 0
    CP3WNetworkReadinessTick()
    if type(CP3WNetworkStatus) ~= "function" then return end
    local status = CP3WNetworkStatus()
    if type(status) ~= "string" or string.len(status) ~= 125 then return end
    local count = tonumber(string.sub(status, 91, 98), 16)
    local attempts = tonumber(string.sub(status, 100, 107), 16)
    local owner = tonumber(string.sub(status, 109, 116), 16)
    if not count or not attempts or not owner then return end
    if owner ~= 0 and count > applied and count == attempts then
        SendEvent("PickupMissileReceived")
    end
    applied = count
end
