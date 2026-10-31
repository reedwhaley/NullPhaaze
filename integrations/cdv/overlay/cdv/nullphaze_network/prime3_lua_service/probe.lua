-- Lua 5.0-compatible, read-only probe executed by the retail LUAX actor. Keep this callback
-- on the retail Lua thread and preserve the exact named event/bridge API used by its
-- matching source builder.
-- Lua 5.0-compatible, read-only probe executed by the retail LUAX actor.
CP3WProbe = {
    schema = 1,
    sequence = 0,
    elapsed = 0,
    interval = 2.5,
    snapshots = 0,
    failures = 0,
    available = false,
    records = {},
    changed = false,
    announced = false,
    change_count = 0,
    notice_elapsed = 6,
    notices = {},
    notice_order = {"ProbeUnavailable", "ProbeReady", "ProbeReadsPassed",
        "ProbeRecovered", "ProbeHeartbeat", "ProbeChanged"},
    items = {"PowerBeam", "Missile", "Energy", "ShipMissile", "SeekerMissile"}
}

local function show_notice()
    if CP3WProbe.notice_elapsed < 6 then return end
    for index, event in ipairs(CP3WProbe.notice_order) do
        if CP3WProbe.notices[event] then
            CP3WProbe.notices[event] = nil
            if event == "ProbeHeartbeat" and CP3WProbe.changed then
                event = "ProbeHeartbeatChanged"
                CP3WProbe.notices.ProbeChanged = nil
            end
            CP3WProbe.notice_elapsed = 0
            SendEvent(event)
            return
        end
    end
end

local function valid_number(value)
    return type(value) == "number" and value == value
        and value >= 0 and value <= 4294967295 and value == math.floor(value)
end

local function sample_inventory()
    local records = {}
    local changed = false
    for index, name in ipairs(CP3WProbe.items) do
        local amount = GetPlayerInventoryAmount(name)
        local capacity = GetPlayerInventoryCapacity(name)
        if not valid_number(amount) or not valid_number(capacity) then
            error("invalid inventory result")
        end
        records[index] = {amount = amount, capacity = capacity}
        local old = CP3WProbe.records[index]
        if old and (old.amount ~= amount or old.capacity ~= capacity) then
            changed = true
        end
    end
    return records, changed
end

function OnThink(dt)
    -- Discard large deltas: loading or pause must never cause a catch-up loop.
    if type(dt) ~= "number" or dt ~= dt or dt < 0 or dt > 1 then
        return
    end
    CP3WProbe.elapsed = CP3WProbe.elapsed + dt
    CP3WProbe.notice_elapsed = CP3WProbe.notice_elapsed + dt
    if CP3WProbe.elapsed < CP3WProbe.interval then
        show_notice()
        return
    end
    CP3WProbe.elapsed = 0

    if not CP3WProbe.announced then
        CP3WProbe.announced = true
        CP3WProbe.notices.ProbeReady = true
    end
    local ok, records, changed = pcall(sample_inventory)
    CP3WProbe.sequence = CP3WProbe.sequence + 1
    if not ok then
        CP3WProbe.failures = CP3WProbe.failures + 1
        if CP3WProbe.available or CP3WProbe.failures == 1 then
            CP3WProbe.notices.ProbeUnavailable = true
        end
        CP3WProbe.available = false
        CP3WProbe.notices.ProbeRecovered = nil
        CP3WProbe.notices.ProbeReadsPassed = nil
        CP3WProbe.notices.ProbeHeartbeat = nil
        show_notice()
        return
    end

    local was_available = CP3WProbe.available
    CP3WProbe.available = true
    CP3WProbe.notices.ProbeUnavailable = nil
    CP3WProbe.records = records
    CP3WProbe.snapshots = CP3WProbe.snapshots + 1
    -- Retail Print is a no-op. A debugger can observe this argument without
    -- adding game networking or invoking any Lua API from a foreign thread.
    local trace = {"CP3W_LUA1", string.format("%.0f", CP3WProbe.sequence)}
    for index, record in ipairs(records) do
        table.insert(trace, string.format("%.0f,%.0f", record.amount, record.capacity))
    end
    Print(table.concat(trace, "|"))
    if CP3WProbe.snapshots == 2 then
        CP3WProbe.notices.ProbeReadsPassed = true
    elseif not was_available and CP3WProbe.snapshots > 2 then
        CP3WProbe.notices.ProbeRecovered = true
    end
    if changed then
        CP3WProbe.changed = true
        CP3WProbe.change_count = CP3WProbe.change_count + 1
        CP3WProbe.notices.ProbeChanged = true
    end
    if math.mod(CP3WProbe.snapshots, 12) == 0 then
        CP3WProbe.notices.ProbeHeartbeat = true
    end
    show_notice()
end
