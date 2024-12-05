def main():
    n = int(input())
    for i in range(n):
        findSol(int(input()))
'''
如果第一個數字為回文，並不算找到顛倒數，要至少加過一次才算。
所以先加過一次再進入while迴圈比較方便!!
'''
def findSol(num):
    num = num + reverse(num) # 與顛倒數相加
    addCount = 1 # 計算相加幾次
    while num != reverse(num): # 如果與顛倒數不同
        num = num + reverse(num) # 與顛倒數相加
        addCount += 1
    print(addCount, num)
    return

# result最右邊加一位數，再加上num的餘數
def reverse(num):
    result = 0
    while num != 0:
        result = result*10 + num%10
        num = num//10
    return result

main()