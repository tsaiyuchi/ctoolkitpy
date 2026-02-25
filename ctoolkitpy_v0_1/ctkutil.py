#--- basic package --- --- ---
from datetime import datetime, date
from traceback import *
import numpy as np
#--- advanced package --- --- ---
import json
from collections import deque
#--- 3rd package --- --- ---
#--- project package --- --- ---


class CtkUtil:

    @staticmethod
    def to_json(obj, indent=4, ensure_ascii=False):
        def default_converter(o):
            if isinstance(o, deque):
                return list(o)
            if isinstance(o, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
                return int(o)
            if isinstance(o, (np.float_, np.float16, np.float32, np.float64)):
                return float(o)
            if isinstance(o, np.ndarray):
                return o.tolist()
            if isinstance(o, (datetime, date)):
                return o.isoformat()
            
            # 5. 其他無法辨識的型別轉為字串
            return str(o)

        return json.dumps(obj, default=default_converter, indent=indent, ensure_ascii=ensure_ascii)
    @staticmethod
    def from_json(json_str): return json.loads(json_str)

    @staticmethod
    def save_json(obj, filepath):
        json_str = CtkUtil.to_json(obj)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
    @staticmethod
    def load_json(filepath):
        if not os.path.exists(filepath): return None
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def from_json_cls(json_str, targe_cls):
        data = CtkUtil.from_json(json_str)
        if not data: return None
        obj = targe_cls()
        obj.__dict__.update(data)
        return obj
    @staticmethod
    def load_json_cls(filepath, targe_cls):
        data = CtkUtil.load_json(filepath)
        if not data: return None
        obj = targe_cls()
        obj.__dict__.update(data)
        return obj
