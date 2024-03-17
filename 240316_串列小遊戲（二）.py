#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:43:44 2024

@author: yitinglu
"""
"""
串列小遊戲（二）：撲克牌 21 點 Black Jack
"""
#程式開始，添加52張牌，洗牌弄亂順序
import random
card = list(range(0,52)) #內容是0~51
random.shuffle(card)

playerCard = list()
playerPoints = list()
bankerCard = list()
bankerPoints = list()

#派兩張牌給玩家，一張給莊家，印出牌面及總點數
def cardPoint(x):   #計算卡牌點數的副程式
    if x % 13 == 0: #A
        return 11
    elif x % 13 > 9: #JQK
        return 10
    else:
        return (x % 13 +1)


def deal(gamerCard, gamerPoints): #派牌副程式
    temp = card.pop() #拿走card中的最後一個數字
    gamerCard.append( temp ) #加到gamer的手牌中
    gamerPoints.append( cardPoint(temp) ) #計算點數
    
def printCard(c): #顯示花色的副程式，c為一個串列
    for i in c:  #每一個串列的東西都拿出來檢視
        if i // 13 == 0:
            print(chr(9824), end="")    #黑桃
        
        elif i // 13 == 1:
            print(chr(9829), end="")    #愛心
            
        elif i // 13 == 2:
            print(chr(9830), end="")    #方塊
        
        else:
            print(chr(9827), end="")    #梅花
            
        if i % 13 == 0:         #牌型
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
            
def printMessage():  #顯示牌面的副程式
    print("玩家的牌： ", end = "")
    printCard(playerCard)
    print("玩家牌面點數：", sum(playerPoints))
    print("莊家的牌： ", end = "")
    printCard(bankerCard)
    print("莊家牌面點數：", sum(bankerPoints))
    print("******************************")



for i in range(2):                      #起始發兩張牌給玩家
    deal(playerCard, playerPoints)

deal(bankerCard, bankerPoints)          #起始發一張牌給莊家

printMessage()

#詢問玩家是否要加牌 <-----------\
#是-->派牌給玩家-->檢查是否爆牌--/
#不加牌-->檢查莊家牌是否小於17點：(<17)派牌給莊家-->檢查是否爆牌

while True: #詢問是否要加牌的迴圈
    ans = input("玩家要加牌嗎？（Y/N）")
    if ans == "N" or ans == "n":
        break
    deal(playerCard, playerPoints)
    if sum(playerPoints) > 21:
        if 11 in playerPoints: #若爆牌：檢查是否有A牌，調整為1，再度詢問玩家（若沒有A牌，裁定莊家獲勝）
            playerPoints[playerPoints.index(11)] = 1
            printMessage() 
        else:
            printMessage()
            print("玩家爆牌，莊家獲勝。")
            break
    else:
        printMessage()

if sum(playerPoints) < 22:
    
    if len(playerPoints) >= 5:
        print("玩家過五，玩家勝利。")
        
    else: 
        
        while sum(bankerPoints) < 17 and len(playerPoints) < 5:
            deal(bankerCard, bankerPoints)
            
            #若莊家爆牌：檢查是否有A牌，調整為1，再度檢查是否17
            
            if sum(bankerPoints) > 21:
                if 11 in bankerPoints:
                    bankerPoints[bankerPoints.index(11)] = 1
            printMessage()    
                
        #若檢查兩者皆未爆牌，比較玩家和莊家點數
        #若兩家牌一樣大，裁定和局
        #程式結束
        
        if sum(bankerPoints) > 21:
            print("莊家爆牌，玩家勝利。")
        elif sum(bankerPoints) > sum(playerPoints):
            print("莊家點數大於玩家，莊家勝利。")
        elif sum(bankerPoints) < sum(playerPoints):
            print("玩家點數大於莊家，玩家勝利。")
        elif sum(bankerPoints) == sum(playerPoints):
            print("和局。")



