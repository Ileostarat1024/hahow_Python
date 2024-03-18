#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:01:28 2024

@author: yitinglu
"""
'''
字串規則與相關函式
'''
'''
Example 1: 密碼規則
輸入密碼，判斷是否符合以下規則：
1. 必須至少含有8個字元
2. 只能含有英文及數字
3. 至少要有一個大寫英文字母
'''
isValid = "密碼正確"
pwd = input("請輸入密碼：")

if len(pwd) < 8:
    isValid = "密碼不符"
if pwd.isalnum() == False:
    isValid = "密碼不符"
    
setAlpha = set(map(chr, range(65,91))) #有沒有大寫字母：想成有沒有和大寫字母的集合有交集
set_pwd = set(pwd)
if len(set_pwd & setAlpha) == 0:
    isValid = "密碼不符"
    
print(isValid)

'''
Exercise 1: 字元對應
使用者輸入字串，顯示每個字串的ASCII Code，以及所有ASCII Code的總和。
'''
string = input("請輸入字串：")
sum_ascii = 0
for i in string:
    print("ASCII code for '{}' is {}".format(i,ord(i)))
    sum_ascii = sum_ascii + ord(i)
print(sum_ascii)











