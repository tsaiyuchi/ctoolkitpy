#--- basic package --- --- ---
from typing import List, Dict, Callable

#--- advanced package --- --- ---
from importlib import metadata
import types


#--- project packages --- --- ---
from .ctklogger import *

class CtkLog:
    map:dict[str, CtkLogger] = {}





    @classmethod
    def get_create(cls, target):
        me = cls
        key = ''
        pkg_to_dist = metadata.packages_distributions()

        if target is None:
            key = ''
        if isinstance(target, str):
            key = target
        elif isinstance(target, type):
            dist = pkg_to_dist.get(target.__module__.split('.')[0])
            key = '' if dist is None else dist[0]
        elif isinstance(target, types.ModuleType): #新增模組情況
            dist = pkg_to_dist.get(target.__name__.split('.')[0])
            key = '' if dist is None else dist[0]
        elif hasattr(target, "__class__"):
            #package也有 __class__ 所以要放在 types.ModuleType 之後
            dist = pkg_to_dist.get(target.__class__.__module__.split('.')[0])
            key = '' if dist is None else dist[0]
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