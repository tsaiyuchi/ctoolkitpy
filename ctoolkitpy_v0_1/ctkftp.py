#--- basci packages


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



class CtkFtp(ftplib.FTP):

    

    def __init__(self, *args, **kwargs):
        me = self
        super().__init__(*args, **kwargs)

        me.config = CtkFtpCfg()
        config = me.config
        config.host = kwargs.get("host", args[0] if args else "")
        config.port = kwargs.get("port", 21) #預設值21
        config.user = kwargs.get("user", "")
        config.passwd = kwargs.get("passwd", "")
    
    def __del__(self):
        try:
            self.quit()
        except Exception:
            pass

    
    def connect_login(self, config:CtkFtpCfg=None):
        me = self
        if(config is not None): me.config = config
        config = me.config

        if not config.host: raise ValueError("Host 未設定，無法連線")
        me.connect(config.host, config.port)
        if config.user: me.login(config.user, config.passwd)
        else: me.login()  # 匿名登入