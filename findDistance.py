# give int d and k
# print all number between 10..0 ~ 99..9 such that 
# largest adajacent digit distance <= k
# 1247 ==> distance = 3
# 9736 ==> distance = 4
# 1111 ==> distance = 0
#  d 代表 幾位數 （d = 4） 需跑 1000 ~ 9999
#  k 代表 在這些數字中 distance < k 的值印出來
#姓名:陳宣閔
#學號:110213018
def main():
    d,k=map(int,input().split())
    #在d位數中,需跑出10**(d-1)到10**d中的所有數.
    for i in range(10**(d-1),10**d):
        #如果每個i值中相鄰兩個數字的差小於k,就輸出.
        if distance(i) <= k:
            print(i)
#算出每個值中相鄰兩個數字的差
def distance(num):
    #慢慢切割出每個值中的每個位數
    # Ex:      num=十位數以上(包含十位數)的數字, pre=個位數, maxD=0
    #     下一輪num=百位數以上(包含百位數)的數字, pre=十位數, maxD=0
    num,pre,maxD=num//10,num%10,0
    while num >0:
        #找出相鄰的兩個位數差的絕對值
        if maxD < abs(num%10-pre):
            maxD=abs(num%10-pre)
        num,pre=num//10,num%10
    return maxD

main()