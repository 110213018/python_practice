# 輸入僅一行包含三正整數，三正整數皆小於 30,001，兩數之間有一空白。
# 輸出共有兩行，第一行由小而大印出此三正整數，兩數字之間以一個空白間格，
# 最後一個數字後不應有空白；第二行輸出三角形的類型：
# 若無法構成三角形時輸出「No」；若構成鈍角三角形時輸出「Obtuse」；
# 若直角三角形時輸出「Right」；
# 若銳角三角形時輸出「Acute」。

def main():
    # input 3 int
    a,b,c = inputData()
    # find solution
    findSol(a,b,c)

#input 3 int, then sort them
def inputData():
    a = int(input())
    b = int(input())
    c = int(input())
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    return a, b, c
    
# check triangle type
def findSol(a, b, c):
    print(a,b,c)
    if a+b <= c:
        print('No')
    elif a*a+b*b < c*c:
        print('Obtuse')
    elif a*a+b*b > c*c:
        print('Acute')
    else:
        print('Rignt')

main()