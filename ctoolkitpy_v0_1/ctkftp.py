#--- basci packages
import os

#--- advanced packages ---
import ftplib
import json

#--- 3rd packages ---

#--- project packages ---


class CtkFtpCfg:
    def __init__(self, host:str=None, port:int=21, user:str=None, passwd:str=None):
        me = self
        me.host = host
        me.port = port
        me.user = user
        me.passwd = passwd

    def to_json(self, indent: int = 4) -> str:
        me = self
        return json.dumps(self.__dict__, indent=indent)

    @classmethod
    def from_json(cls, data: str):
        cfg_dict = json.loads(data)
        return cls(**cfg_dict)

    def save_to_file(self, file_path: str):
        me = self
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(me.to_json())
    @classmethod
    def load_from_file(cls, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"找不到設定檔: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        return cls.from_json(data)



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
