# -*- coding: UTF-8 -*-

globvar = 0

def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print (globvar)        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量


'''
1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。
2、一个global语句可以同时定义多个变量，如 global x, y, z。
'''