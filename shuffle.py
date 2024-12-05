# 姓名:陳宣閔
# 學號:110213018
# 發橋牌
# 假設以int 0~51表示52張牌
# 0~12為spade A~2,13~25為heart, 26~38 diamond, 39~51 club
# 請發East, South, West,North
# East
# S AKQ32
# H
# D AJT987
# C 32
# South
# S ...
# H ...
# 亂數發四張牌
import random
# return a list contains 4 lists
def shuffle():
    card = [i for i in range(52)] # create new cards, card=[0,1,2,3...,51]
    # shuffle cards by swap 2 cards many times
    for i in range(1000):
        # randint(): 會產生指定範圍內的隨機整數
        x,y = random.randint(0,51),random.randint(0,51) # x,y = 隨機兩張牌
        card[x],card[y] = card[y],card[x] # 洗牌
    return [sorted(card[:13]),sorted(card[13:26]),sorted(card[26:39]),sorted(card[39:])] #分別按照順序,回傳隨機排序好的牌(位置0~12,13~25,26~38,38~51),且每一組要按a,k,q~2排好

def showCards(hands):
    # print four hand cards
    # how to print?
    for h in range(4): # 四個玩家
        print(['North','East','South','West'][h]+':')
        for s in range(4): # 四個花色
            print(['S','H','D','C'][s],end=' ')
            print(sameSuit(s,hands[h]))# 換列
# s= 四個花色
# card= 每個人分到的牌
def sameSuit(s,card):
    name = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    result=''
    for c in card: # print v of suit s
        if c//13==s: # 商數:判斷花色
            result += name[c%13] #餘數:判斷牌面的數字
    return result

def main():
    showCards(shuffle())

main()