#--- basci packages
import os
#--- advanced packages ---
import ftplib
import json
#--- 3rd packages ---
#--- project packages ---
from .ctkutil import *

class CtkFtpCfg:
    def __init__(self, host:str=None, port:int=21, user:str=None, passwd:str=None):
        me = self
        me.host = host
        me.port = port
        me.user = user
        me.passwd = passwd

    def to_json(self, indent:int=4)->str: return CtkUtil.to_json(self)
    def save_json(self, filepath:str): CtkUtil.save_json(self, filepath)
    @classmethod 
    def from_json(cls, json_str: str): return CtkUtil.from_json_cls(json_str, cls)
    @classmethod
    def load_json(cls, filepath:str): return CtkUtil.load_json_cls(filepath, cls) 





class CtkFtp(ftplib.FTP):

    def __init__(self, host: str = "", user: str = "", passwd: str = "", port: int = 21, timeout: int = 30):
        me = self
        # 初始化父類別，但不立即連線 (若要立即連線可將參數傳入 super)
        super().__init__(timeout=timeout)
        
        me.config = CtkFtpCfg(
            host=host,
            port=port,
            user=user,
            passwd=passwd
        )
    
    
    def connect_login(self, config:CtkFtpCfg=None):
        me = self
        if(config is not None): me.config = config
        config = me.config

        if not config.host: raise ValueError("Host 未設定，無法連線")
        me.connect(config.host, config.port)
        if config.user: me.login(config.user, config.passwd)
        else: me.login()  # 匿名登入


#region Dispose --- --- ---
    def dispose_close(self):
        me = self
        try: me.quit()
        except: me.close()
    def __del__(self): self.dispose_close()
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): self.dispose_close()
#endregion Dispose --- --- ---
