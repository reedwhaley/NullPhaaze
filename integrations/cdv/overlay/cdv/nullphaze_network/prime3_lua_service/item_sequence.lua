-- Private compiled grant sequence. No diagnostic HUD or framebuffer rendering. Keep this
-- callback on the retail Lua thread and preserve the exact named event/bridge API used by
-- its matching source builder.
-- Private compiled grant sequence. No diagnostic HUD or framebuffer rendering.
local elapsed = 0
local applied = 0
function OnThink(dt)
    if type(dt) ~= "number" or dt ~= dt or dt <= 0 or dt > 1 then return end
    elapsed = elapsed + dt
    if elapsed < 0.5 then return end
    elapsed = 0
    CP3WReceiptProbeTick()
    CP3WNetworkReadinessTick()
    local status = CP3WNetworkStatus()
    if type(status) ~= "string" or string.len(status) ~= 125 then return end
    local count = tonumber(string.sub(status, 91, 98), 16)
    local attempts = tonumber(string.sub(status, 100, 107), 16)
    if count and count > applied and count == attempts and count <= 16 then
        SendEvent("SequenceReceived" .. tostring(count))
    end
    applied = count or applied
end
