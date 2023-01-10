import os
import time
from shutil import copy

#creates hidden copy of output csv
def hidden_copy(file_name):
    copy_name = file_name+time.strftime("_%Y%d%m_%H%M%S", time.localtime())
    copy(r"extracted/{}.csv".format(file_name), "bkp/{}".format(copy_name))
