#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:04:35 2024

@author: yitinglu
"""
'''
進階流程控制（二）：猜密碼遊戲
設計一程式，亂數取1~100內的數字（含）當作密碼，使使用者不斷猜測至猜中為止。

使用者每猜一個數字，程式會把範圍縮小，若使用者再猜出此範圍外，會顯示超出範圍
的訊息。若猜測落在範圍內，則程式會把範圍繼續縮小，直到猜出答案。
'''
import random
answer = random.randint(1,100)

minimum = 1
maximum = 100
guess = int(input("請輸入 1~100 間的數字："))

while guess != answer:
    
    if guess >= minimum and guess < answer:
        minimum = guess + 1
        guess = int(input("沒猜中，請繼續輸入 {}~{} 間的數字：".format(minimum, maximum)))
        continue
    if guess <= maximum and guess > answer:
        maximum = guess - 1
        guess = int(input("沒猜中，請繼續輸入 {}~{} 間的數字：".format(minimum, maximum)))
        continue
    if guess < minimum or guess > maximum:
        guess = int(input("猜測數字超出範圍，請繼續輸入 {}~{} 間的數字：".format(minimum, maximum)))
        continue    
print("答對了，密碼就是：", answer)

