# -*- coding: UTF-8 -*-

def add(x,y):
  return x+y

def add_twice(func,x,y):
  return func(func(x,y),func(x,y))##计算过程(5+10)+(5+10)

a=5
b=10

print(add_twice(add,a,b))