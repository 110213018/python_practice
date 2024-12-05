# 姓名:陳宣閔
# 學號:110213018

# row是橫的(列)
# column是直的(行)
def main():
    n=int(input())
    #一列一列被回傳之後會形成方陣
    for r in magic(n):
        print(*myFormat(r,n)) #去掉括弧逗號

#一次處理一列
def magic(n):
    result = [[0 for j in range(n)] for i in range(n)] #先把n*n方陣中的數字都設為0
    r,c = 0,n//2 #找出第一列中間的位置
    result[r][c] = 1 #第一列的中間為1
    for v in range(2,n*n+1):
        nextr,nextc = (r-1)%n,(c+1)%n #下一個數字在往上一列,往右一行
        if result[nextr][nextc] != 0: #如果已經有數字
            nextr,nextc = (r+1)%n,c   #就在數字下方印出下一個數字
        r,c,result[nextr][nextc] = nextr,nextc,v 
    return result

def myFormat(data,n):
    for v in data:
        yield str(v).zfill(len(str(n*n))) #zfill : 只能處理字串,與其他數對齊個位數,空缺處補0
                                          #yield : 不斷回傳至第9列,直到東西傳完才結束,並存成一個list

main()