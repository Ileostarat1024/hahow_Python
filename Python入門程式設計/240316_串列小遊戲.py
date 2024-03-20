#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:08:57 2024

@author: yitinglu
"""
'''
串列遊戲製作 1A2B
'''
#程式開始，亂數取4位數密碼（範圍0~9)
#兩個變數，計算A和B的總數量
#計算輸入的密碼是否為4A0B-->若是：程式結束，恭喜答對
#--> 若否：詢問玩家輸入密碼，確認是4位不同的數字（若否，重新跳回這個迴圈詢問）
#--> 玩家成功輸入後，計算A,B數量，輸出結果（偵測，是否4A（跳回此區首））

import random
list_pwd = range(0,10)
answer = random.sample(list_pwd, 4)
a = 0
b = 0

while a != 4:
    
    a = 0
    b = 0
    
    guess = input("請輸入四位數密碼：")
    
    while len(guess) != 4 or len(set(guess)) < 4:
        guess = input("請輸入四位數密碼（必須輸入剛好四位且數字不可重複）：")
    
    ans_check = list(map(int, guess))
    
    for i in ans_check: #這裡的 i 則會套用成所有 list 內的項目
        if i in answer: 
            if ans_check.index(i) == answer.index(i):
                a += 1
            else:
                b += 1
                
    print("你猜的答案為："+str(a)+"A"+str(b)+"B")

print("答對了，密碼就是", guess)
    






