# -*- coding: UTF-8 -*-

def reverse(li):
    for i in range(0, int(len(li)/2)):
        li[i], li[-i - 1] = li[-i - 1], li[i]

l = [1, 2, 3, 4, 5]
reverse(l)
print(l)