
#--- basic packages ---
from datetime import datetime

#--- project packages
from .ctkloglevel import *


class CtkLogEntity:
    message: str
    exception: Exception
    traceback_msg: str
    level: CtkLogLevel
    log_object: object
    record_datetime: datetime

    def __init__(self, message:str=None, exception:Exception=None, traceback_msg:str=None, level: CtkLogLevel=None, log_object:object=None):
        me = self
        me.message = message
        me.exception = exception
        me.traceback_msg = traceback_msg
        me.level = level
        me.log_object = log_object
        me.record_datetime = datetime.now()





