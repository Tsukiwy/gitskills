# -*- coding: UTF-8 -*-
#获取当前时间 

import time
 
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)


'''
本地时间为 : time.struct_time(tm_year=2018, tm_mon=12, tm_mday=17, tm_hour=8, tm_min=15, tm_sec=39, tm_wday=0, tm_yday=351, tm_isdst=0)
'''