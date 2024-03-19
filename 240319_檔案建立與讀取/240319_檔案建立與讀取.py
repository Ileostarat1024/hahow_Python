#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:36:34 2024

@author: yitinglu
"""
'''
檔案建立與讀取

Example 1: 資料加總
撰寫程式，讀取 24_1data.txt 的內容，內容為數字以空白做分隔，將這些數字加總後印出。
'''
fobj = open("24_1data.txt", "r", encoding="utf-8")
content = fobj.read().split(" ")
fobj.close()

num_sum = sum(map(int,content))
print("數字加總為：", num_sum)

'''
Exercise 1: 資料取代
撰寫程式，讀取 24_2data.txt 的內容，改寫pen成sneakers 至 24_2dataＷrite 檔案中.txt，
並印出。
'''
fobj = open("24_2data.txt", "r", encoding="utf-8")
content = fobj.read()
fobj.close()

content = content.replace("pen","sneakers")

fobj = open("24_2dataWrite.txt","w")
fobj.write(content)
fobj.close()

fobj = open("24_2dataWrite.txt", "r", encoding="utf-8")
content = fobj.read()
fobj.close()

print(content)


