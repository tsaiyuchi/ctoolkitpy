#--- basic package --- --- ---
from datetime import datetime
from traceback import *
#--- advanced package --- --- ---
#--- 3rd package --- --- ---
#--- project package --- --- ---


class CtkTimeUtil:



#region sign1 --- --- ---

    @staticmethod
    def tosign1_year(dt:datetime): return dt.strftime("y%Y")
    @staticmethod
    def tosign1_quarter(dt: datetime):
        quarter = (dt.month - 1) // 3 + 1
        return f"q{dt.year}{quarter}"
    @staticmethod
    def tosign1_month(dt: datetime): return dt.strftime("m%Y%m")
    @staticmethod
    def tosign1_week(dt: datetime):return dt.strftime("w%Y%U")
    @staticmethod
    def tosign1_day(dt: datetime):return dt.strftime("d%Y%m%d")

#endregion sign1 --- --- ---



#region sign3 --- --- ---

    @staticmethod
    def tosign3_day(dt:datetime): return dt.strftime("day%Y%m%d")

    @staticmethod
    def tosign3_minute(dt:datetime): return dt.strftime("min%Y%m%d%H%M")

    @staticmethod
    def tosign3_hour(dt: datetime): return dt.strftime("hr_%Y%m%d%H")

#endregion sign3 --- --- ---
