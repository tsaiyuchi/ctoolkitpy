#--- basic packages ---
from enum import Enum
from datetime import datetime
from typing import List, Callable
import time
import traceback

#--- advanced packages --- --- ---
from threading import Thread, Lock, Event
import asyncio

#--- 3rd packages ---

#--- projec packages ---


class ECtkLogLevel(Enum):
    NoDefine = 0
    Verbose = 1
    Debug = 2
    Info = 3
    Warn = 4
    Error = 5
    Fatal = 6



class CtkLogEntity:
    message: str
    exception: Exception
    traceback_msg: str
    level: ECtkLogLevel
    caller: object #可以是 object or type or None
    record_datetime: datetime

    def __init__(self, message:str=None, exception:Exception=None, traceback_msg:str=None, level: ECtkLogLevel=None, caller:object=None):
        me = self
        me.message = message
        me.exception = exception
        me.traceback_msg = traceback_msg
        me.level = level
        me.caller = caller
        me.record_datetime = datetime.now()




class CtkLogger:
    is_disposed : bool
    name: str
    lock : Lock
    logs : List[CtkLogEntity]
    thread : Thread
    eh_logwrite: List[Callable]
    eh_logwrite_global: List[Callable] = []

    def __init__(self):
        me = self
        me.is_disposed = False
        me.name = None
        me.lock = Lock()
        me.logs = []
        me.thread = None
        me.eh_logwrite = []

    def __del__(self):
        me = self
        me.dispose()

    def dispose(self):
        me = self
        me.is_disposed = True

    #common writing entry
    def write(self, entity:CtkLogEntity):
        me = self
        me.logs_append(entity);
        if(me.thread == None or not me.thread.is_alive()):
            me.thread = Thread(target=me.run_loop)
            me.thread.start()
    #regular write use a message
    def write_message(self, message:str, level:ECtkLogLevel=ECtkLogLevel.Info, caller:object=None, exception:Exception=None, traceback_msg:str=None):
        me = self
        entity = CtkLogEntity(message, exception, traceback_msg, level, caller)
        me.write(entity)
    #regular write use a exception
    def write_exception(self, exception:Exception, traceback_msg:str=None, level:ECtkLogLevel=ECtkLogLevel.Warn, caller:object=None, message:str=None):
        me = self
        entity = CtkLogEntity(message, exception, traceback_msg, level, caller)
        me.write(entity)

    def logs_append(self, entity: CtkLogEntity):
        me = self
        try:
            me.lock.acquire()
            me.logs.append(entity)
        finally:
            me.lock.release()
    def logs_pop(self):
        me = self
        try:
            me.lock.acquire()
            if(me.logs): return me.logs.pop(0)
            return None
        finally:
            me.lock.release()

    def run_loop(self):
        me = self
        while(not me.is_disposed and me.logs):
            try:
                me.run_once()
            except Exception as ex:
                #just print if logging happen exception, 也沒其它方法
                print(ex)
                traceback.print_exc() #traceback.format_exc()
    def run_once(self):
        me = self
        entity = me.logs_pop()
        if(entity == None):return
        for func in me.eh_logwrite:
            if(func == None): continue
            func(me, entity)
        for func in me.eh_logwrite_global:
            if(func == None): continue
            func(me, entity)

