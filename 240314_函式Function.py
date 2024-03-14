#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:43:25 2024

@author: yitinglu
"""
'''
Example 1: 次方函數
撰寫一程式，使用者輸入兩個數當引數，呼叫名為 power(x,y) 的函式，回傳
x的y次方結果並印出。

範例輸入：
請輸入底數數字：3
請輸入次方數字：4
範例輸出：
3 的 4 次方為 81
'''
def power(x,y):
    return x**y

a = int(input("請輸入底數數字："))
b = int(input("請輸入次方數字："))

print("{} 的 {} 次方為 {}".format(a,b,power(a,b)))

'''
Exercise 1: 開 n 次方根函數
撰寫一程式，使用者輸入兩個數當引數，呼叫名為 nroot(x,y) 的函式，回傳
x開y次方根的結果並印出。

範例輸入：
請輸入被開方數字：64
請輸入開方數字：6
範例輸出：
64 開 6 次方為 2
'''
def nroot(x,y):
    return x ** (1/y)

def decimal_check(num):
    return float(num).is_integer()

a = int(input("請輸入被開方數字："))
b = int(input("請輸入開方數字："))
if b == 0:
    print("開方數字不得為 0。")
else:
    result = nroot(a,b)

    if decimal_check(result) == True:
        print("{} 開 {} 次方為 {}。".format(a,b,int(result)))

    else:
        print("{} 開 {} 次方為 {:.3f}。".format(a,b,result))

'''
Example 2: 求一元二次方程式的解
撰寫一程式，使用者輸入ax^2+bx+c=0中的a,b,c，求 x 的數。若無解則顯示無解。
'''
def equation (a,b,c):
    d = b**2 - 4*a*c
    if d > 0:
        m = (-b + d**(1/2))/(2*a)
        n = (-b - d**(1/2))/(2*a)
        return str(m)+" ,"+str(n)
    elif d == 0:
        m = -b/(2*a)
        return str(m)+" 重根"
    else:
        return "無解"

input_a = eval(input("請輸入方程式係數 a："))
input_b = eval(input("請輸入方程式係數 b："))
input_c = eval(input("請輸入方程式係數 c："))
print("此方程式的解為 "+ equation(input_a,input_b,input_c))
        
'''
自己寫的答案（過於複雜）：
def discriminant(a,b,c):
    return b**2 - 4*a*c

while True:
    input_a = eval(input("請輸入方程式係數 a："))
    input_b = eval(input("請輸入方程式係數 b："))
    input_c = eval(input("請輸入方程式係數 c："))
    if discriminant(input_a, input_b, input_c) >= 0:
        solution1 = (-input_b + (input_b**2-4*input_a*input_c)**(1/2))/(2*input_a)
        solution2 = (-input_b - (input_b**2-4*input_a*input_c)**(1/2))/(2*input_a)
        if solution1 == solution2:
            print("方程式的解為",solution1)
        else:
            print("方程式的解為",solution1,",",solution2)
    else:
        print("此方程式無解")
'''
'''
Exercise 2: 質數
撰寫一程式，使用者可以不斷輸入整數，以該整數為引數呼叫 primeTest() 這個函式。
此函數回傳字串顯示「質數」或「非質數」，直到使用者輸入-9999結束測試。
（負數皆為非質數）

範例輸入：
97
91
-5
-9999
範例輸出：
97 為質數
91 為非質數
-5 為非質數
'''
#思考：一個數的平方根是自己（潛在）最大的因數，因此只要確定平方根以下除了1以外
#的任何數都沒辦法除盡自己，即可確定是質數。

def primeTest(a):
    if a < 0:
        return "非質數"
    else:
        for i in range(2, int(a**0.5)+1, 1):
            if a%i == 0:
                return "非質數"
        return "質數"
    

while True:
    userInput = int(input("請輸入整數(輸入-9999結束程式）："))
    if userInput == -9999:
        break
    if userInput == 1 or userInput == 0:
        print(str(userInput) + " 為非質數")
        continue
    else:
        print("{} 為 {}".format(userInput, primeTest(userInput)))
print("輸入-9999，程式已結束。")

'''
Example 3: 最大公因數
撰寫一程式，使用者輸入兩個整數 a,b，作為引數呼叫 gcd()函式，並回傳兩數的
最大公因數。

＊用輾轉相除法的原理
讓一數的餘數成為原本除數的除數：原本有被除數n和除數m，經過一次除法之後，
除數m變成被除數（n的位置），餘數(n%m)變成除數(m的位置)，直到某次餘數為0，
下次開始，被除數仍然存在，但是除數變成0（m的位置），n 就是 gcd


範例輸入：
52,91 (中間以逗點做分隔)
範例輸出：
52 和 91 的最大公因數為 13。
'''
def gcd(n,m):
    if m == 0:
        return n
    else: 
        return gcd(m, n%m)

num1,num2 = (input("請輸入兩個整數，中間用逗點做分隔：").split(","))
num1 = int(num1)
num2 = int(num2)

print("{} 和 {} 的最大公因數為 {}".format(num1, num2, gcd(num1,num2)))





