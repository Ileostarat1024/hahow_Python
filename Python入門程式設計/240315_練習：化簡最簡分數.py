#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:45:29 2024

@author: yitinglu
"""
'''
Exercise: 化簡最簡分數
撰寫一程式，讓使用者輸入兩個分數，m/n,x/y，皆為正整數，
計算m/n+x/y的結果，並以最簡分數表示。

範例輸入：
請輸入第一個分數的分子分母：5,6
請輸入第二個分數的分子分母：3,10
範例輸出：
5/6 + 3/10 = 17/15
'''
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def irreducibleFraction(a,b):
    if gcd(a,b) == 1 and b != 1:
        return str(a)+"/"+str(b)
    elif b == 1:
        return str(a)
    else:
        return irreducibleFraction(int(a/gcd(a,b)),int(b/gcd(a,b)))
    
        
def lcd_add(a,b,c,d): #least common denominator addition
    if gcd(b,d) == 1:
        return irreducibleFraction(((a*d)+(c*b)),(b*d))
    else:
        denominator = int(b*(d/gcd(b,d)))
        numerator1 = int(a*(d/gcd(b,d)))
        numerator2 = int(c*(b/gcd(b,d)))
        return irreducibleFraction((numerator1+numerator2),denominator)

m,n = input("請輸入第一個分數的分子分母（用逗點分隔）：").split(",")
x,y = input("請輸入第二個分數的分子分母（用逗點分隔）：").split(",")
m,n,x,y = int(m),int(n),int(x),int(y)
if n == 0 or y == 0:
    print("分母不可為 0")
else:
    print("算式結果如下：{}/{} + {}/{} = {}".format(m,n,x,y,lcd_add(m,n,x,y)))

