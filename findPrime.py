#學號:110213018
#姓名:陳宣閔
def main():
    begin = int(input())#輸入第一個數字
    end=int(input())#輸入最後一個數字
    #如果第一個數字大於最後的數字,則交換順序
    if begin > end :
        begin,end=end,begin
    printPrimes(begin,end)

# print all primes <= end
def printPrimes(begin,end):
    # print begin from 1 to end
    while begin <= end:
        #如果條件式為true,則輸出begin
        if isPrime(begin):
            print(begin)
        #while迴圈結果為true,則begin+1接到下一個數字繼續執行,直到false(begin>end)
        begin = begin+1 
        
# test if begin is a prime
def isPrime(begin):
    #除1 and begin都不能整除begin
    div = 2 
    while div < begin:
        if begin % div == 0:
            return False
        div = div + 1
    return True

main()

