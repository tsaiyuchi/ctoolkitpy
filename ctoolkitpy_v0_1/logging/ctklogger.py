
#--- advanced package ---
from typing import List, Callable
import time
from threading import Thread, Lock, Event
import traceback

#--- 3rd packages ---
from events import Events

#--- projec packages ---
from .ctkloglevel import *
from .ctklogentity import *


class CtkLogger:

    is_disposed : bool
    name: str
    lock : Lock
    logs : List[CtkLogEntity]
    thread : Thread
    thread_stop_event:Event
    eh_logwrite: List[Callable]
    eh_logwrite_global: List[Callable] = []

    def __init__(self):
        me = self
        me.is_disposed = False
        me.name = None
        me.lock = Lock()
        me.logs = []
        me.thread = None
        me.thread_stop_event = Event()
        me.eh_logwrite = []
    def __del__(self):
        me = self
        me.dispose()
    def dispose(self):
        me = self
        me.is_disposed = True
        me.thread_stop_event.set()

    #common writing entry
    def write(self, entity:CtkLogEntity):
        me = self
        try:
            me.lock.acquire()
            me.logs.append(entity)
            if(me.thread == None or not me.thread.is_alive()):
                me.thread = Thread(target=me.run_loop)
                me.thread.start()

        finally:
            me.lock.release()

    #regular write use a entity creation
    def write_log(self, message:str=None, exception:Exception=None, traceback_msg:str=None, level:CtkLogLevel=None, log_object:object=None):
        me = self
        entity = CtkLogEntity(message, exception, traceback_msg, level, log_object)
        me.write(entity)
    #regular write use a message
    def write_message(self, message:str, exception:Exception=None, traceback_msg:str=None, level:CtkLogLevel=CtkLogLevel.Info, log_object:object=None):
        me = self
        me.write_log(message, exception, traceback_msg, level, log_object)
    #regular write use a exception
    def write_exception(self, exception:Exception, message:str=None, traceback_msg:str=None, level:CtkLogLevel=CtkLogLevel.Warn, log_object:object=None):
        me = self
        me.write_log(message, exception, traceback_msg, level, log_object)


    def pop(self):
        me = self
        try:
            me.lock.acquire()
            if(me.logs): return me.logs.pop(0)
            return None
        finally:
            me.lock.release()

    def run_loop(self):
        me = self
        while(not me.is_disposed and not me.thread_stop_event.is_set() and me.logs):
            try:
                me.run_once()
            except Exception as ex:
                #just print if logging happen exception
                print(ex)
                traceback.print_exc()

    def run_once(self):
        me = self
        log = me.pop()
        if(log == None):return

        for func in me.eh_logwrite:
            if(func == None): continue
            func(me, log)

        for func in me.eh_logwrite_global:
            if(func == None): continue
            func(me, log)












