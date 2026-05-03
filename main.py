import win32evtlog
import win32evtlogutil
from functions import read_log

def main():
    server = "localhost"
    log_names = ["System"]
    output_file = "system_log.txt"

    all_events = []

    for log_name in log_names:
        events = read_log(server, log_name)
        print(f"Opened: {log_name}")
        print(f"Read from {log_name}: {len(events)}")
        all_events.extend(events)

    with open(output_file, "w", encoding="utf-8") as f:
        for event in all_events:
            f.write(
                f"Event ID: {event ['event_id']}\n"
                f"Source: {event['source']}\n"
                f"Time: {event['time']}\n"
                f"Type: {event['type']}\n"
                f"{'-' * 40}\n"
            )

    print(f"Events: {len(all_events)}")
    print(f"Writing to: {output_file}")

if __name__ == "__main__":
    main()

