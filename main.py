import os
import win32evtlog
import win32evtlogutil
from functions import read_log

server = "localhost"
log_type = "System, Security, Application"

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
hand = win32evtlog.OpenEventLog(server, log_type) # Read the server and log_type variables

try:
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    for event in events[:1]:
        print(f"Time {event.TimeGenerated}")
        print(f"ID: {event.EventID}")
        print(f"Category: {event.EventCategory}")
finally:
    win32evtlog.CloseEventLog(hand)

