#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:44:56 2024

@author: yitinglu
"""
'''
List 串列

Example 1: 計算撲克牌牌面總和
'''
card = ['0','A','2','3','4','5','6','7','8','9','10','J','Q','K']
total = 0
for i in range(1,6):
    temp = input("請輸入第 "+str(i)+" 個牌面的值：")
    total += card.index(temp)
print("牌面總和為 "+str(total))

'''
Exercise 1: 奇數索引值加總
輸入10個整數，依序存入串列中，列出奇數索引值加總。
'''
list1 =list()
total = 0
for i in range(1,11):
    temp = int(input("請輸入第 "+str(i)+" 個整數:"))
    list1.append(temp)
for j in range(1,11,2):
    total += list1[j]
print("奇數索引值的加總為 "+str(total))

'''
Exercise 2: 成績計算
輸入10個成績，印出最高分、最低分、總和成績、平均成績
'''
scores = list()
for i in range(1,11):
    temp = int(input("請輸入第 "+str(i)+" 個成績："))
    scores.append(temp)
print("最高分的成績為："+str(max(scores)))
print("最低分的成績為："+str(min(scores)))
print("成績總和為："+str(sum(scores)))
print("成績平均為："+str(sum(scores)/len(scores)))

'''
Example 2: 計算出現最多次的數字，以及出現次數
'''
#使用者輸入10個數字，並儲存於串列中
list1 = list()
for i in range(1,11):
    temp = int(input("請輸入第 "+str(i)+" 個數字："))
    list1.append(temp)
#計算每個數字出現的次數
count = list()
for j in range(10):
    count.append(list1.count(list1[j]))
most_count = max(count)
most_num = list1[count.index(max(count))]
#列印結果
print("數字 {} 出現最多次，出現 {} 次".format(most_num,most_count))

'''
Exercise 3: 數字排序
輸入10個數字，由大到小排序，輸出最大的三個數字及最小的三個數字。
'''
#使用者輸入10個數字
num_list = list()
for i in range(1,11):
    temp = int(input("請輸入第 "+str(i)+" 個數字："))
    num_list.append(temp)
#排序由大到小
num_list.sort(reverse = True)
#印出前三個和後三個
print("最大三個數：",num_list[:3])
print("最小三個數：",num_list[-3:])







