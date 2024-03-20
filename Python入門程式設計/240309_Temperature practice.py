#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:38:25 2024

@author: yitinglu
"""

cdegree = eval(input("請輸入攝氏溫度值： "))
fdegree = cdegree * (9/5) +32
fdegree = round(fdegree, 2)
print( "攝氏溫度", cdegree, "度，相當於華氏溫度", fdegree, "度。")