
#--- advanced package ---
from typing import List
from threading import Thread, Lock

#--- 3rd packages ---
from events import Events

#--- projec packages ---
from .ctkloglevel import *
from .ctklogentity import *


class CtkLogger:

    lock : Lock
    logs : List[CtkLogEntity]
    thread : Thread
    is_disposed : bool


    def __init__(self):
        me = self
        me.lock = Lock()
        me.logs = []
        me.thread = Thread(me.run)
        me.is_disposed = False

        me.thread.start()
    def __del__(self):
        me = self
        me.dispose()




    def write(self, entity:CtkLogEntity):
        me = self
        try:
            me.lock.acquire()
            me.logs.append(entity)
        finally:
            me.lock.release()

    def write_message(self, message:str, level:CtkLogLevel=CtkLogLevel.Info, log_object:object=None):
        me = self
        entity = CtkLogEntity(message=message, level=level, log_object=log_object)
        me.write(entity)

    def write_exception(self, exception:Exception, level:CtkLogLevel=CtkLogLevel.Info, log_object:object=None):
        me = self
        entity = CtkLogEntity(exception=exception, level=level, log_object=log_object)
        me.write(entity)


    def pop(self):
        me = self
        try:
            me.lock.acquire()
            if(me.logs): return me.logs.pop(0)
            return None
        finally:
            me.lock.release()

    def run(self):
        me = self

        while(not me.is_disposed):
            log = me.pop()






    def dispose(self):
        me = self
        me.is_disposed = True







