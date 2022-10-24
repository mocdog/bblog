import os
import time

ret = os.fork()
pid = os.getpid()
if ret == 0:
    while True:
        print("process run on child pid:", pid)
        time.sleep(1)
else:
    while True:
        print("process run on main pid:", pid)
        time.sleep(1)