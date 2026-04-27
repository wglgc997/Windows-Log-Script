import os
import win32evtlog
import win32evtlogutil
from functions import read_log

server = "localhost"
log_type = "System, Security, Application"

read_log(server, log_type)




