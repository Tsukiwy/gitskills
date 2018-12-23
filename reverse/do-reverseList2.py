# -*- coding: UTF-8 -*-

def reverse(ListInput):
    RevList=[]
    for i in range (len(ListInput)):
        RevList.append(ListInput.pop())
    print(RevList)
    return RevList

l = [1, 2, 3, 4, 5]
reverse(l)
print(l)