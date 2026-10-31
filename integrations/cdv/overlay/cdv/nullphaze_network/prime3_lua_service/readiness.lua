-- Separate grant-free hardware readiness gate; only retail Lua drives it. Keep this callback
-- on the retail Lua thread and preserve the exact named event/bridge API used by its
-- matching source builder.
-- Separate grant-free hardware readiness gate; only retail Lua drives it.
local CP3WOriginalThink = OnThink
local CP3WNetworkElapsed = 0
function OnThink(dt)
    CP3WOriginalThink(dt)
    if type(dt) ~= "number" or dt ~= dt or dt <= 0 or dt > 1 then return end
    CP3WNetworkReadinessDraw()
    CP3WNetworkElapsed = CP3WNetworkElapsed + dt
    if CP3WNetworkElapsed < 0.5 then return end
    CP3WNetworkElapsed = 0
    CP3WNetworkReadinessTick()
end
