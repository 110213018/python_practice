#學號:110213018
#姓名:陳宣閔

#輸入每個人(data)
def main():
    data = list(map(int,input().split()))
    findfriend(data)

#人按排序,編號分別為0 1 2....最後一人.
#判斷有幾個小團體
def findfriend(data):
    mark = [0 for i in range(len(data))] #標記位置 CF:一開始mark=[0,0,0,...]一旦data跟v相同位置判斷過,就變成-1.
    count = 0 #計算小團體數量,從零開始算起
    #v=編號
    for v in range(len(mark)):
        #如果被標記過,就繼續
        if mark[v] == -1:
            continue
        #如果人與相同位置之編號數相同,count就+1,且列印.
        if data[v] == v:
            count += 1
            print(v)
        #如果都不是就跳到下一個function.
        else:
            count += findgroup(data,mark,data[v],v)
    print("小團體數:",count)

#找出-1 #找出誰和誰是朋友
def findgroup(data,mark,pos,v):
    group = ""                    #group為小團體,先把group用成空字串
    group = group + str(v) + ' '  #在小團體中的每個人後面加上空白建,除去最後一人
    mark[v] = -1                  #標記過的為-1
    while data[pos] != v:         #如果人與相同位置之編號數不相同
        mark[pos] = -1            #就將此位置標記成-1
        group = group + str(pos) + ' '  #在空字串加上符合的人跟空白建
        pos = data[pos]           #找到下一個編號(pos變成下一個編號)
    mark[pos] =-1                 #因為小團體中的最後一位好友不符合while迴圈,就幫標記
    group = group + str(pos)      #因為小團體中的最後一位好友不符合while迴圈,所以把他加進小團體
    print(group)                  #輸出每一組小團體
    return 1                      #將值回傳至25,小團體數(count)就會+1
main()