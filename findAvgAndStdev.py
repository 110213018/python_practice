#學號:110213018
#姓名:陳宣閔
def statistic(data):
    #計算出平均數
    sum=0
    ammount=0
    for i in data:
        sum=sum+i #計算出list中的值總和
        ammount=ammount+1#計算出list中的數值個數總和
    avg=sum/ammount#平均數等於list中的值總和除以list中的數值個數總和
    #計算出標準差
    sigma=0
    for v in data:
        sigma=sigma+(v-avg)**2#標準差根號中的分子
    stdev=(sigma/ammount)**0.5#標準差公式
    return avg,stdev #回傳至35列

def main():
    data=list()#輸入一列表
    try:
        while True:
            data=data+list(map(float,input().split()))#將列表中的元素分隔
    except EOFError:
        pass
    avg,stdev=statistic(data)
    print(avg,stdev) #列印平均值跟標準差

main()
