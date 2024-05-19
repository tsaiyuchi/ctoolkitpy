
#--- basic packages ---
from datetime import datetime

#--- project packages
from .ctkloglevel import *


class CtkLogEntity:
    message: str
    exception: Exception
    level: CtkLogLevel
    record_datetime: datetime
    log_object: object

    def __init__(self, message:str=None, level: CtkLogLevel=CtkLogLevel.Info, exception:Exception=None, log_object:object=None):
        me = self
        me.message = message
        me.level = level
        me.exception = exception
        me.record_datetime = datetime.now()
        me.log_object = log_object





