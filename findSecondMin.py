#姓名:陳宣閔
#學號:110213018
#input a set of int
#5 3 2 8 66 3 7 4
#data:a list of int
#returns:the second minimun distance between adjacent int

# 1.
def main():
    data=list()#輸入一列表
    data=data+list(map(int,input().split()))#分割元素
    secmin=findSecondMin(data)
    print(secmin)#輸出第二小的絕對值

def findSecondMin(data):
    min=abs(data[1]-data[0])#先設一個最小絕對值
    secmin=abs(data[2]-data[1])#先設一個第二小絕對值
    #要確保預設的兩個數min一定要小於secmin,如果預設的min大於secmin,就交換.
    if min>secmin:
        min,secmin=secmin,min
    #找出真正的第二小絕對值
    for i in range(3,len(data)):
        if abs(data[i]-data[i-1])<min:#如果abs(data[i]-data[i-1])小於預設的min,它就變成min,然後在回圈中一直比較.
            min=abs(data[i]-data[i-1])
        if min<abs(data[i]-data[i-1])<secmin:#如果abs(data[i]-data[i-1])介於min和secmin之間,它就變成secmin,然後在回圈中一直比較.
            secmin=abs(data[i]-data[i-1])
    
    return secmin#回傳至第10列
main()

# 2.
def main():
    x = list(map(int, input().split()))
    x.sort(reverse = True)
    result = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i>=j:
                continue
            else:
                result.append(abs(x[i]-x[j]))
    result.sort()
    print(result[1])

main()