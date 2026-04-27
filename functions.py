import win32evtlog
import subprocess
from pathlib import Path


def read_log(server, log_type):
    readLog = (win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ)
    eventLogList = win32evtlog.OpenEventLog(server, log_type)

    try:
        events = win32evtlog.ReadEventLog(eventLogList, readLog, 0 )
        for event in events[:10]:
            print(f"Time {event.TimeGenerated}")
            print(f"ID: {event.EventID}")
            print(f"Category: {event.EventCategory}")
            print("--" * 10)
    finally:
        win32evtlog.CloseEventLog(eventLogList)

def create_file():
    file_path = Path(r'C:\Users\ResTIC55\PycharmProjects\WinLogProject')
    log_file =  file_path / "system_log.txt"
    backup_file =  file_path / "backup.txt"

    file_path.mkdir(parents=True, exist_ok=True)
    log_file.write_text("Teste")





