#--- basic package --- --- ---
from datetime import datetime
from traceback import *
#--- advanced package --- --- ---
#--- 3rd package --- --- ---
#--- project package --- --- ---


class CtkTimeUtil:


    @staticmethod
    def tosign3_day(dt:datetime): return dt.strftime("day%Y%m%d")

    @staticmethod
    def tosign3_minute(dt:datetime): return dt.strftime("min%Y%m%d%H%M")


