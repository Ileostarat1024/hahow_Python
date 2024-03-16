#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:53:38 2024

@author: yitinglu
"""
'''
List 2 串列二
'''
'''
Example 1: 大樂透
系統隨機從1~49中抽出6個號碼，以及1個特別號(數字不可重複），並將之從小排到大輸出。
'''
import random
lotto_list = list()
#亂數選取7個號碼，拿掉最後一個當作特別號
for i in range(7):
    temp = random.randint(1,49)
    #注意：要判斷該值有沒有重複（=已經被取過），有就要繼續random
    while temp in lotto_list:
        temp = random.randint(1,49) #重新取，直到temp not in lotto_list
    lotto_list.append(temp)

special = lotto_list.pop()
#lotto_list.sort()
print("本次樂透開獎號碼為：", sorted(lotto_list))
print("特別獎為：", special)

'''
小試身手：在串列中建立'A'到'Z'
'''
AZ_list = list()
for i in range(ord("A"), ord("Z")+1):
    AZ_list.append(i)
AZ_list = list(map(chr, AZ_list))
print(AZ_list)

#更簡化的版本
example = list(map(chr, range(65,91))) #range本身就是形成一個串列; list用來顯示map地址的內容
print(example)
'''
map 功能操作：將串列裡的元素作三次方（提示：另外寫一個函式）
'''
def triple(a):
    return a**3

original_list = [1,2,3,4,5]
transformed_list = list(map(triple, original_list)) #若不想放參數，函式後面不要括弧
print(transformed_list)



