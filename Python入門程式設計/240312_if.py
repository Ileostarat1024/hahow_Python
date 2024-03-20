#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:09:17 2024

@author: yitinglu
"""

'''
if - Practice: BMI calculation
'''
sex = input("請問你的性別是（男生填 M / 女生填 F)：")
height = eval(input("請問你的身高是（單位：公分）："))
weight = eval(input("請問你的體重是（單位：公斤）："))
bmi = weight / (height/100)**2

if sex == "M":
    if bmi > 25:
        print("體重過重。")
    elif bmi >=20 and bmi <= 25:
        print("身材適中。")
    elif bmi <20:
        print("體重過輕。")
    else:
        print("輸入錯誤，請重試。")

elif sex == "F":
    if bmi > 22:
        print("體重過重。")
    elif bmi >=18 and bmi <= 22:
        print("身材適中。")
    elif bmi <18:
        print("體重過輕。")
    else:
        print("輸入錯誤，請重試。")
        
else:
    print("發生錯誤，請重試。")
    
'''
Exercise (1): Input a, b and calculate 輸入數字及運算符
'''
a, b = int(input("請輸入正整數 a：")), int(input("請輸入正整數 b："))
calculator = input("請輸入任一運算子（+,-,*,/,//,%,**）：")

if calculator == "+":
    print("{} + {} = {}".format(a,b,a+b))
elif calculator == "-":
     print("{} - {} = {}".format(a,b,a-b))
elif calculator == "*":
     print("{} * {} = {}".format(a,b,a*b))
elif calculator == "/":
    if b != 0:
     print("{} / {} = {}".format(a,b,a/b))
    else:
     print("錯誤：除數不可為 0")
elif calculator == "//":
    if b != 0:
     print("{} // {} = {}".format(a,b,a//b))
    else:
     print("錯誤：除數不可為 0")
elif calculator == "%":
    if b != 0:
     print("{} % {} = {}".format(a,b,a%b))
    else:
     print("錯誤：除數不可為 0")
elif calculator == "**":
     print("{} ** {} = {}".format(a,b,a**b))
else:
    print("發生錯誤，請重試。")
    
'''
Exercise (2): leap year 閏年判斷
'''
year = int(input("請輸入西元年份："))

if year % 100 != 0:
    if year % 4 == 0:
        print("{} 是閏年。".format(year))
    else:
        print("{} 不是閏年。".format(year))
elif year % 100 ==0:
    if year % 400 == 0:
        print("{} 是閏年。".format(year))
    else:
        print("{} 不是閏年。".format(year))


    
    
    
