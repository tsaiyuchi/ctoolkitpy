#--- basic package --- --- ---
import os
from datetime import datetime, date
from traceback import *
import numpy as np
#--- advanced package --- --- ---
import json
from collections import deque
#--- 3rd package --- --- ---
#--- project package --- --- ---


class CtkUtil:

    @staticmethod #僅參考、用原生也只一行，帶入常用參數
    def to_json(obj, indent=4, ensure_ascii=False, default=None): return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii, default=default)
    @staticmethod #僅參考、用原生也只一行
    def from_json(json_str): return json.loads(json_str)
    @staticmethod
    def from_json_cls(json_str, targe_cls):
        data = CtkUtil.from_json(json_str)
        if not data: return None
        obj = targe_cls()
        obj.__dict__.update(data)
        return obj

    @staticmethod
    def save_json(filepath, obj, indent=4, ensure_ascii=False, default=None):
        json_str = json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii, default=default)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)
    @staticmethod
    def load_json(filepath):
        if not os.path.exists(filepath): return None
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    @staticmethod
    def load_json_cls(filepath, targe_cls):
        data = CtkUtil.load_json(filepath)
        if not data: return None
        obj = targe_cls()
        obj.__dict__.update(data)
        return obj
