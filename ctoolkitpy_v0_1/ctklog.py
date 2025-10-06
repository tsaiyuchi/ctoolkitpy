#--- basic package --- --- ---
from typing import List, Dict, Callable

#--- project packages --- --- ---
from .ctklogger import *

class CtkLog:
    map:dict[str, CtkLogger] = {}

    @classmethod
    def get_create(cls, target):
        me = cls
        key = ''
        if target is None:
            key = ''
        if isinstance(target, str):
            key = target
        elif isinstance(target, type):
            key = f'{target.__module__}'
        elif hasattr(target, "__class__"):
            key = target.__class__.__module__
        else: raise Exception('Error target')

        if key in me.map: return me.map[key]
        logger = CtkLogger()
        logger.name = key
        me.map[key] = logger
        return logger


    @classmethod
    def write(cls, entity:CtkLogEntity, target = None):
        me = cls
        if(entity == None): return #passing without log
        logger = me.get_create(target)
        logger.write(entity)

    @classmethod
    def info(cls, message:str=None, target=None, exception=None, traceback_msg=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Info, target)
        cls.write(entity, target)
    @classmethod
    def info_ex(cls, exception:Exception, traceback_msg:str=None, target:object=None, message:str=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Info, target)
        cls.write(entity, target)

    @classmethod
    def warn(cls, message:str=None, target=None, exception=None, traceback_msg=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Warn, target)
        cls.write(entity, target)
    @classmethod
    def warn_ex(cls, exception:Exception, traceback_msg:str=None, target:object=None, message:str=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Warn, target)
        cls.write(entity, target)

    @classmethod
    def error(cls, message:str=None, target=None, exception:Exception=None, traceback_msg:str=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Error, target)
        cls.write(entity, target)
    @classmethod
    def error_ex(cls, exception:Exception, traceback_msg:str=None, target:object=None, message:str=None):
        entity = CtkLogEntity(message, exception, traceback_msg, ECtkLogLevel.Error, target)
        cls.write(entity, target)



    @classmethod
    def add_event(cls, func:Callable, target):
        me = cls
        logger = me.get_create(target)
        logger.eh_logwrite.append(func)

    @classmethod
    def add_event_global(cls, func:Callable):
        me = cls
        CtkLogger.eh_logwrite_global.append(func)