# -*- coding: UTF-8 -*-
#获取格式化的时间

 
import time
 
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)


'''
本地时间为 : Mon Dec 17 08:19:57 2018
'''