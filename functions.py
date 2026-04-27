import win32evtlog

def read_log(server,log_type):
    flags = (win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ)
    handle = win32evtlog.OpenEventLog(server,log_type)

    try:
        events = win32evtlog.ReadEventLog(handle, flags, 0)
        for event in events[:10]:
            print(f"Time {event.TimeGenerated}")
            print(f"ID: {event.EventID}")
            print(f"Category: {event.EventCategory}")
            print("--" * 10)
    finally:
        win32evtlog.CloseEventLog(handle)