
#--- basic package --- --- ---
from typing import List, Dict, Callable

#--- project packages --- --- ---
from .logging.ctklogger import *


class CtkLog:

    map:dict[str, CtkLogger] = {}

    @classmethod
    def get_create(cls, key:str):
        me = cls
        if key in me.map: return me.map[key]
        logger = CtkLogger()
        logger.name = key
        me.map[key] = logger
        return logger

    @classmethod
    def cal_key(cls, aname:str=None, aobject:object=None, atype:type=None):
        me = cls
        key = aname
        if(key == None and aobject != None): atype = type(aobject)
        if(key == None and atype != None): key = f'{atype.__module__}.{atype.__name__}'
        if(key == None): key = ''
        return key

    @classmethod
    def write(cls, entity:CtkLogEntity, aname:str=None, aobject:object=None, atype:type=None):
        me = cls
        if(entity == None): return #passing without log
        key = me.cal_key(aname, aobject, atype)
        logger = me.get_create(key)
        logger.write(entity)

    @classmethod
    def write_log(cls, message:str=None, exception:Exception=None, traceback_msg:str=None, level:CtkLogLevel=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        me = cls
        if(message == None and exception == None): return #passing without log
        key = me.cal_key(aname, aobject, atype)
        logger = me.get_create(key)
        logger.write_log(message, exception, traceback_msg, level, log_object)



    @classmethod
    def info(cls, message:str=None, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Info, log_object, aname, aobject, atype)
    @classmethod
    def info_msg(cls, message:str, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Info, log_object, aname, aobject, atype)
    @classmethod
    def info_ex(cls, exception:Exception, message:str=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Info, log_object, aname, aobject, atype)

    @classmethod
    def warn(cls, message:str=None, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Warn, log_object, aname, aobject, atype)
    @classmethod
    def warn_msg(cls, message:str, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Warn, log_object, aname, aobject, atype)
    @classmethod
    def warn_ex(cls, exception:Exception, message:str=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Warn, log_object, aname, aobject, atype)

    @classmethod
    def error(cls, message:str=None, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Error, log_object, aname, aobject, atype)
    @classmethod
    def error_msg(cls, message:str, exception:Exception=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Error, log_object, aname, aobject, atype)
    @classmethod
    def error_ex(cls, exception:Exception, message:str=None, traceback_msg:str=None, log_object:object=None
                  , aname:str=None, aobject:object=None, atype:type=None):
        cls.write_log(message, exception, traceback_msg, CtkLogLevel.Error, log_object, aname, aobject, atype)



    @classmethod
    def add_event(cls, func:Callable, aname:str=None, aobject:object=None, atype:type=None):
        me = cls
        key = me.cal_key(aname, aobject, atype)
        logger = me.get_create(key)
        logger.eh_logwrite.append(func)
    @classmethod
    def add_event_global(cls, func:Callable):
        me = cls
        CtkLogger.eh_logwrite_global.append(func)
