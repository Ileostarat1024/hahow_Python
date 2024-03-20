#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:28:41 2024

@author: yitinglu
"""
'''
Exercise 1: 撰寫一程式，使用者輸入數字，直到使用者輸入 9999 作為結束為止，
印出所有輸入值中的最小值。
'''
i = 1
j = 1
print("請輸入數字，直到 9999 結束。")
while True:
    num = int(input("請輸入第{}個整數：".format(i)))
    #num = int(input("請輸入第"+str(i)+"個整數"))
    
    while j ==1:
        min_num = num
        j += 1
    
    i += 1
    if num == 9999:
        break
    if num >= min_num:
        continue
    min_num = num
    
print("程式結束，您剛才輸入的數字中，最小值為", min_num)

'''
參考解法：
count = 1 
minimunm = int(input("請輸入第"+str(count)+"個整數"))
userInput = minimum

while userInput != 9999:
    if userInput < minimum:
        userInput = minimum
    count += 1
    userInput = int(input("請輸入第"+str(count)+"個整數"))
print("程式結束，您剛才輸入的數字中，最小值為", minimum)
'''

'''
Exercise 1.5: 撰寫一程式，使用者輸入數字，直到使用者輸入 9999 作為結束為止，
印出所有輸入值中的最大值（不包含9999）。
'''
print("請輸入數字，若輸入9999則結束程式。")

count = 1
maximum = int(input("請輸入第"+str(count)+"個整數："))
userInput = maximum

while userInput != 9999:
    if userInput > maximum:
        maximum = userInput
    count += 1
    userInput = int(input("請輸入第"+str(count)+"個整數："))
print("程式結束，已輸入的最大值為", maximum)



'''
Exercise 2: 撰寫一程式，使用者輸入一正整數，則輸出此正整數的反轉順序，
直到輸入 9999 結束。

＊重點：字串索引值
若s1 = "abc"
則s1[0] == "a"

＊重點：字串長度
len(s1) == 3
'''
print("請輸入數字，若輸入9999則結束程式。")
userInput = (input("請輸入任一正整數："))

while userInput != "9999":
    
    print("您輸入的數字 "+userInput+" 反轉後為： ", end = "")
    for i in range(len(userInput)-1, -1, -1):
        print(userInput[i], sep = "", end = "")
    print()
    userInput = (input("請輸入任一正整數："))
    
print("輸入9999，程式結束。")

#參考解法：
print("請輸入數字，若輸入9999則結束程式。")
count = 1 

while True:
    userInput = (input("請輸入任一正整數："))
    result = ""
    if userInput == "9999":
        break
    for i in range(len(userInput)):
        result = userInput[i] + result
    print("您輸入的數字 "+userInput+" 反轉後為： "+result)
    
print("輸入9999，程式結束。")

'''
Exercise 2.5: 輸入的數字各項加總
'''
print("請輸入數字，若輸入999則結束程式。")

while True:
    num = input("請輸入數字：")
    num_sum = 0
    result = ""
    
    if num == "9999":
        break
    for i in range(len(num)):
        result = result + num[i]
        if i <len(num)-1:
            result = result + "+"
    for j in range(len(num)):
        num_sum = int(num[j]) + num_sum
    print("您輸入的數字 "+num+" 的各項加總結果："+result+"="+str(num_sum))
    
print("輸入9999，程式結束。")

'''
Exercise 3: 倍數的個數與總和

使用者輸入兩個正整數 a, b (a<=b)，輸入這兩個正整數（包含）間，
7 或 11 的倍數（一列輸出 10 個數字，欄寬為 4，靠左對齊），以及倍數的個數
與總和。
#範例輸入：起始值 9, 結束值 99
#範例輸出：
11 14....49
55 56....98
99
總數共有 21 個
數字總和為 1146
'''
a = int(input("請輸入起始值："))
b = int(input("請輸入結束值："))
count = 1
num_sum = 0

for num in range(a, b+1, 1):
    if num % 7 !=0 and num % 11 !=0:
        continue
    print("{:<4}".format(num), end = " ")
    if count % 10 == 0:
        print()
    count += 1
    
    num_sum = num + num_sum
    
print()
print("總數共有 {} 個".format(count-1))
print("數字總和為 {}".format(num_sum))
    
    
    
    
    


