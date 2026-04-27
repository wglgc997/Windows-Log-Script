import win32evtlog
import win32evtlogutil
from functions import create_file, read_log

server = "localhost"
log_type = "System, Security, Application"

read_log(server, log_type)
create_file()