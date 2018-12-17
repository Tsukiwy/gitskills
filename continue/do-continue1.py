# -*- coding: UTF-8 -*-
'''
continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分
'''
var = 10

while var > 0:
    var = var -1
    if var == 5 or var == 8:
        continue
    print ("当前值 :", var)
print ("Good bye!")


'''
当前值 : 9
当前值 : 7
当前值 : 6
当前值 : 4
当前值 : 3
当前值 : 2
当前值 : 1
当前值 : 0
Good bye!
'''