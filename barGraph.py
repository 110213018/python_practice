# 姓名:陳宣閔
# 學號:110213018

# print()       換行
# print(end='') 不換行

def main():
    n = int(input()) #輸入總共要輸入幾個數字
    num = list(map(int,input().split())) #輸入數字列表
    FindGra(n,num)

#做出表格
def FindGra(n,num):
    for i in range(max(num)+2,0,-1): #y軸為num中最大值+2
        print(str(i).zfill(2),end=' ') #輸出y軸,每個數與其他數對齊個位數,空缺處補0
        FinGra2(i,num)
        print()
    line_x(n,num)

#找出#跟..
def FinGra2(i,num):
    for j in range(len(num)):
        if i <= num[j]:          #如果y軸的值小於等於num列表中的值,就輸出##
            print('## ',end='')
        else:                    #沒有,就輸出..
            print('.. ',end='')
#輸出x軸
def line_x(n,num):
    for v in range(len(num)+1):
        print(str(v).zfill(2),end=' ') #每個數與其他數對齊個位數,空缺處補0
main()