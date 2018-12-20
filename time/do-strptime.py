# -*- coding: UTF-8 -*-
#格式化日期

 
import time
 
# 格式化成2018-12-17 08:24:57形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
 
# 格式化成Mon Dec 17 08:24:57 2018形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
  
# 将格式字符串转换为时间戳
a = "Mon Dec 17 08:24:57 2018"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


'''
2018-12-17 08:25:40
Mon Dec 17 08:25:40 2018
1545035097.0
'''