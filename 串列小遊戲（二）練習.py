#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:40:34 2024

@author: yitinglu
"""
#9824 黑桃 / 9829 愛心 / 9830 方塊 / 9827 梅花
#程式開始，添加52張牌，洗牌弄亂順序，內容是0~51
import random
card = list(range(0,52))
random.shuffle(card)

playerCard = []
playerPoint = []
bankerCard = []
bankerPoint = []
#派兩張牌給玩家，一張給莊家，印出牌面及總點數
#計算卡牌點數的副程式
def cardPoint(x):
    if x % 13 == 0:
        return 11
    if x % 13 > 9:
        return 10
    else:
        return (x%13 +1)

#派牌副程式
def deal(gamerCard, gamerPoint):
    temp = card.pop()
    gamerCard.append(temp)
    gamerPoint.append(cardPoint(temp))

#顯示花色的副程式，c為一個串列(#每一個串列的東西都拿出來檢視)
def printCard(c):
    for i in c:
        if i // 13 == 0:
            print(chr(9824), end="")
        elif i // 13 == 1:
            print(chr(9829), end="")
        elif i // 13 == 2:
            print(chr(9830), end="")
        else: 
            print(chr(9827), end="")
        if i % 13 == 0:
            print('A', end=" ")
        elif i % 13 == 10:
            print('J', end=" ")
        elif i % 13 == 11:
            print('Q', end=" ")
        elif i % 13 == 12:
            print('K', end=" ")
        else:
            print(i%13+1, end=" ")
    print()

#顯示牌桌面的副程式
def cardMessage():
    print("玩家的牌： ", end=" ")
    printCard(playerCard)
    print("玩家的總點數：", sum(playerPoint))
    print("莊家的牌：", end=" ")
    printCard(bankerCard)
    print("莊家的總點數：",sum(bankerPoint))
    print("*************************")

#起始發兩張牌給玩家，一張給莊家
for i in range(2):
    deal(playerCard, playerPoint)
    
deal(bankerCard, bankerPoint)

cardMessage()
#詢問玩家是否要加牌 <-----------\
#是-->派牌給玩家-->檢查是否爆牌--/
#不加牌-->檢查莊家牌是否小於17點：(<17)派牌給莊家-->檢查是否爆牌
#若爆牌：檢查是否有A牌，調整為1，再度詢問玩家（若沒有A牌，裁定莊家獲勝）
while True:
    
    if len(playerPoint) == 5:
        print("玩家過五，玩家勝利。")
        break
    
    ans = input("是否要繼續加牌？（Y/N）")
    
    if ans == 'N' or ans == 'n':
        break
    
    
    deal(playerCard, playerPoint)
    if sum(playerPoint) > 21:
        if 11 in playerPoint:
            playerPoint[playerPoint.index(11)] = 1
            cardMessage()
        else:
            cardMessage()
            print("玩家爆牌，莊家勝利。")
            break
    else:
        cardMessage()

if sum(playerPoint) < 22:
    
    while sum(bankerPoint) <17 and len(playerPoint) < 5:
        
        deal(bankerCard, bankerPoint)
        #若莊家爆牌：檢查是否有A牌，調整為1，再度檢查是否17
        if sum(bankerPoint) > 21:
            if 11 in bankerPoint:
                bankerPoint[bankerPoint.index(11)] = 1
    cardMessage()
                
#若檢查兩者皆未爆牌，比較玩家和莊家點數
#若兩家牌一樣大，裁定和局
#程式結束
    if sum(bankerPoint) > 21:
        print("莊家爆牌，玩家勝利。")
    elif sum(bankerPoint) > sum(playerPoint):
        print("莊家點數大於玩家，莊家勝利。")
    elif sum(bankerPoint) < sum(playerPoint):
        print("玩家點數大於莊家，玩家勝利。")
    elif sum(bankerPoint) == sum(playerPoint):
        print("和局。")

    

        
 
 







