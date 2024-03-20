# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
格式化輸出練習
'''
floatA = 3.1415926
print("The answer is {}".format(floatA))

'''
d 是用在整數值; f 是用在浮點數
'''
print("The answer is {:10f}".format(floatA))
print("The answer is {:>10f}".format(floatA))
print("The answer is {:<10f}".format(floatA))
print("The answer is {:^10f}".format(floatA))

print("The answer is {:.3f}".format(floatA))
print("The answer is {:+.3f}".format(floatA))
print("The answer is {:.0f}".format(floatA))

'''
{:number.3f} - number 指預留的位數
'''
print("The answer is {:10.3f}".format(floatA))

'''
空位補記號
'''
print("The answer is {:0>10f}".format(floatA))
print("The answer is {:x<12f}".format(floatA))

'''
特殊符號
'''
intA = 123456789
print("I want to earn {:,}".format(intA))
print("I want to earn {:.5%}".format(intA))
print("I want to earn {:.5e}".format(intA))

'''
Examples and Practices 1
Calculate the distance of two points
'''
x1,y1 = eval(input("請輸入 A 點 x 座標：")), eval(input("請輸入 A 點 y 座標："))
x2,y2 = eval(input("請輸入 B 點 x 座標：")), eval(input("請輸入 B 點 y 座標："))
distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
print ("A 點({0},{1})與 B 點({2},{3})的距離為 {4:.4f} ".format(x1,y1,x2,y2,distance))


