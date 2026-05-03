import win32evtlog

def read_log(server,log_name):
    eventList = [] # Logs will be storage in this list
    eventOrder = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ # read  the logs from the newer for the oldest

    try:
        eventOpen = win32evtlog.OpenEventLog(server, log_name) # Open  the connection with event viewer

    except Exception as e:
        print(f"Failed to open event log {log_name} : {e}")
        return []

    while True:
        events = win32evtlog.ReadEventLog(eventOpen, eventOrder, 0) # Read the event log

        if not events: # If don't have logs, stop the code
            break

        for event in events: # Organize the format and save in the list.
            eventList.append({
                "event_id": event.EventID,
                "source": event.SourceName,
                "time": str (event.TimeGenerated),
                "type": event.EventType})

    return eventList