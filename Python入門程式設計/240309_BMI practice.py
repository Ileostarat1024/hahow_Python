#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:26:41 2024

@author: yitinglu
"""
height = eval (input ("請輸入身高(單位：公分）： "))
weight = eval (input ("請輸入體重（單位：公斤）： "))

'''
bmi = str(weight / (height/100)**2)
print ("此人的 BMI 為： " + bmi)
'''

bmi = weight / (height/100)**2
print ("此人的 BMI 為： " ,bmi)

