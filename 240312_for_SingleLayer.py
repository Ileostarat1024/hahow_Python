#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:59:24 2024

@author: yitinglu
"""

'''
for - Practice: Print @ triangles
'''

n = int(input("請輸入正整數 n："))
for i in range(n):
    print("@"*(i+1))
    
'''記得字串*數字，就是重複字串內容的意思'''

for i in range(n):
    print(" "*(n-i) + "*"*(i+1))

for i in range(n):
    print("$"*(n-i))

'''
Print isosceles triangle
'''
m = int(input("請輸入等腰三角形的層數："))
for i in range(1,m+1,1):
    print(" "*(m-i+15) + "%"*(2*i-1) + " "*(m-i))
for j in range(3,m+3,1):
    print(" "*(m-j+15) + "%"*(2*j-1) + " "*(m-j))
for k in range(5,m+5,1):
    print(" "*(m-k+15) + "%"*(2*k-1) + " "*(m-k))
for p in range(2):
    print(" "*(m+13) + "%"*3 + " "*(m+13))
    
''' 
Thinking process

    % 1 (1+0) 3 -i=1
   %%% 3 (2+1) 2 -i=2
  %%%%% 5 (3+2) 1 -i=3
 %%%%%%% 7 (4+3) 0 -i=4
'''

'''
Print 9 * 9 chart
'''
n = int(input("請輸入想查詢的九九乘法表數字："))
for i in range(1,10):
    print("{} * {} = {}".format(n, i, n*i))
    

    
