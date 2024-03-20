#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:52:43 2024

@author: yitinglu
"""
'''
Tuple 數組：用小括號表示

Example 1: 串列與數組的轉換
使用者輸入整數存於串列，直至-9999為止，將串列轉為數組，算出長度、最大最小值、總和。
'''
list1 = list()
i = 1
while True:
    num = int(input("請輸入第 "+str(i)+" 個數："))
    i = int(i)
    i += 1
    if num != -9999:
        list1.append(num)
    else:
        break

tuple1 = tuple(list1)

print(tuple1)
print("長度為", len(tuple1))
print("最大值為", max(tuple1))
print("最小值為", min(tuple1))
print("總和為", sum(tuple1))

'''
Set 集合：用大括號表示

宣告要用 set() (不能用{} --> 這是詞典的形式)
< = > 等符號表示的是包含關係（不是長度關係）
沒有索引[]功能
'''
'''
Example 1: 子集合與超集合
使用者分別輸入4, 3, 7個整數，儲存至s1, s2, s3中，輸出s2是否為s1的子集合，
以及s3是否為s1的超集合。
'''
#切割出來的結果是list, 重新轉換成set
s1 = set(input("請輸入第 1 個集合（4個數）：").split(" "))
s2 = set(input("請輸入第 2 個集合（3個數）：").split(" "))
s3 = set(input("請輸入第 3 個集合（7個數）：").split(" "))

print("集合2是集合1的子集合：", s2 <= s1)
print("集合3是集合1的超集合：", s3 >= s1)

'''
Dict 詞典

Example 1: 詞典合併
使用者輸入兩個詞典（key入end表示一個詞典的結束點，詞典不包含end），後將兩詞典合併，
依照字母順序排列key，若有重複key值，第二個詞典覆蓋第一個。
'''
dict1 = dict()
print("請輸入第一個詞典：")
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict1[key] = value

dict2 = dict()
print("請輸入第二個詞典：")
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict2[key] = value
    
dict1.update(dict2)
print("以下為兩個詞典合併的結果：")

for i in sorted(dict1.keys()):
    print(i, ':', dict1[i], sep = "")
    
    
    
    
    
    
    
    
    
    
    

    















