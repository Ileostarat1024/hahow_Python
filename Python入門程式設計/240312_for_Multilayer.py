#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:47:49 2024

@author: yitinglu
"""
'''
Exercise 1: Print Octal-numbers
'''
for i in range(0,8):
    for j in range(0,8):
        print("{}{} ".format(i,j))
        
'''print(要印出來的東西, sep = "預設一個空格", end = "\n 預設印完之後換行")'''
'''print 指令本身就有換行的效果'''
'''故以上範例修改成：'''
for i in range(0,8):
    for j in range(0,8):
        print(i, j, sep = "", end = " ")
    print()

'''
Exercise 2: Print decreasing-number triangle (1-9, 1-8,...1)
'''
for i in range(10,0,-1):
    for j in range(1,i):
        print(j, end = " ")
    print()

'''
Exercise 3: Print number triangle (1-9, 2-9,...9)
'''
for i in range(1,10):
    for j in range(i,10):
        print(j, end = " ")
    print()
    
'''
Exercise 4: Print increasing-number triangle (1,1-2,1-3,...1-9)
'''
for i in range(10,0,-1):
    for j in range (1,11-i):
        print(j, end =" ")
    print()
    

'''
Exercise 5: Print number triangle (1,2-1,3-1,...9-1)
'''
for i in range(2,11):
    for j in range(i-1, 0, -1):
        print(j, end = " ")
    print()

'''
Exercise 6: Print full 9*9 chart
'''
for i in range(1,10):
    for j in range(2,10):
        print("{}*{}={:<2}".format(j,i,i*j), end = " ")
    print()
    
'''乘出來的結果要預留兩個位數，才能對齊（加上靠左）'''








