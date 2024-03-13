#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:14:32 2024

@author: yitinglu
"""
"""
while - Practice
"""
i = 1
n = int(input("請輸入任一正整數："))
while i < n+1:
    print("@"*i)
    i += 1

'''
Random 模組：需要匯入，產生亂數
'''
import random
random.randint(1,50)

for i in range (0,10):
    print(random.randint(1,50))

'''
盲猜密碼 Exercise
'''
import random
pw = random.randint(0,9)
guess = eval(input("請輸入密碼(0~9)： "))
while guess != pw:
    guess = eval(input("猜錯，再猜(0~9)："))
print("答對了！密碼就是", pw)

# 迴圈內某種條件成立，跳出一層迴圈：使用 break
# 迴圈內某種條件成立，希望部分程式不要執行，但繼續跑回圈：使用 continue

'''
列印亂數：列印 1 到 20 的亂數，不列印 5 的倍數，列印到 11 就結束。
'''
import random

while True: #希望迴圈一直不斷執行
    randnum = random.randint(1,20) #亂數必須要再迴圈裡做，才能一直產生新亂數
    if randnum == 11:
        print(randnum)
        break
    elif randnum % 5 == 0:
        print(randnum, "hehe")
        continue
    else:
        print(randnum)










