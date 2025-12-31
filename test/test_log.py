
#--- basic package --- --- ---
import os,inspect,sys
import traceback

#--- advanced package --- --- ---
from pathlib import Path

#--- 3rd package --- --- ---
from ctoolkitpy_v0_1 import *

#--- project package --- --- ---
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir) # add parent folder for import parent package



CtkLog.get_create(CtkLog)
CtkLog.get_create(CtkLog())
CtkLog.get_create(ctklog)


