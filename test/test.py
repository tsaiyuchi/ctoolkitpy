
#--- basic packages --- --- ---
import sys
import os
from datetime import datetime



#--- appending parent packages --- --- ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ctoolkitpy_v0_1.ctklog import *


def log_write(obj, log:CtkLogEntity):
    now = datetime.now()
    print(f"\
[{now.strftime('%Y-%m-%d %H:%M:%S')}][{log.level.name}] \
message={log.message if log.message!=None else ''}; \
exception={log.exception if log.exception!=None else ''}; \
traceback={log.traceback_msg if log.traceback_msg!=None else ''}"
)

CtkLog.add_event_global(log_write)


CtkLog.info_msg('aaa', Exception('bbb'), 'ccc')



