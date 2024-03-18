#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:43:08 2024

@author: yitinglu
"""
'''
Example 1: 數組合併排序
輸入兩個數組，輸入數字的中間用空白隔開，兩數組合併後列印，再重新排數組由小到大列印。
'''
list1 = input("請輸入第一個數組：").split(" ")
tuple1 = tuple(map(int, list1))
list2 = input("請輸入第二個數組：").split(" ")
tuple2 = tuple(map(int, list2))

print("數組合併：", tuple1+tuple2)
print("排列後的數組：", sorted(tuple1+tuple2))

'''
Exercise 1: 數組條件判斷
使用者輸入五個以上的字串進入數組中，以空白作間隔，輸出數組，並輸出前三個與後三個元素。
'''
list1 = input("請輸入數組（至少五個以上的元素）：").split(" ")
tuple1 = tuple(list1)
tuple1_first3 = tuple(list1[:3])
tuple1_final3 = tuple(list1[-3:])
    
print("數組內容：", tuple1)
print("數組前三項：", tuple1_first3)
print("數組後三項：", tuple1_final3)

'''
Example 2: 全字母句判斷
輸入一個句子，程式判斷是否為全字母句（全部英文字母都用上），每句列印判斷結果，
直到輸入end。
'''
setAlpha = set(map(chr, range(97,123)))
print("請輸入句子以測試是否為全字母句，輸入 end 結束。")

while True:
    temp = input()
    if temp == 'end':
        break
    setUser = set(temp.lower()) #全部轉成小寫
    if len(setUser & setAlpha) == 26:
        print("此句為全字母句。")
    else:
        print("此句為不是全字母句。")
        
'''
Exercise 2: 共同興趣
使用者分別輸入A和B的興趣，以空白做分隔。依序顯示：
1. A和B所有的興趣
2. A和B共有的興趣
3. A和B彼此沒有的興趣
4. A有B沒有的興趣
輸出時內容字母由小排到大
'''
set_A = set(input("請輸入 A 的興趣：").split(" "))
set_B = set(input("請輸入 B 的興趣：").split(" "))

print("A 與 B 的所有興趣為：", sorted(set_A | set_B))
print("A 與 B 的共有興趣為：", sorted(set_A & set_B))
print("A 與 B 彼此沒有的興趣：", sorted(set_A ^ set_B))
print("A 有但 B 沒有的興趣：", sorted(set_A - set_B))

'''
Example 3: 詞典排序
使用者輸入一個顏色詞典，key鍵入end表示結束，依字母大小順序輸出：
'''
print("請輸入顏色詞典，輸入 Key 值為 end 時程式結束。")
color_dict = dict()
while True:
    temp = input("Key: ")
    if temp == 'end':
        break
    color_dict[temp] = input("Value: ")

for i in sorted(color_dict.keys()):
    print(i,": ",color_dict[i], sep="")

'''
Exercise 3: 詞典搜尋
英漢辭典，end 結束輸入，提示搜尋單字若單字不存在，顯示單字不存在，若存在，顯示
中文。
'''
print("請輸入英漢辭典（中文為Key，英文為Value），若輸入end則程式結束。")
en_dict = dict()

while True:
    enWord = input("英文單字： ")
    if enWord == 'end':
        print()
        break
    chWord = input("中文意思： ")
    en_dict[enWord] = chWord

while True:
    search = input("請輸入想要查找的單字意思： ")
    if search == 'end':
        break
    answer = en_dict.get(search, "單字不存在")
    print(answer)















