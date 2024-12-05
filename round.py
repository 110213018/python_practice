'''
取v值小數點第n位四捨五入
取到小數點第2位四捨五入,1.234 ==> 1.23, 1.235 ==> 1.24

四捨五入:
int(1.4+0.5) --> 1
int(1.5+0.5) --> 2

'''
def main():
    v = float(input())
    n = int(input())
    ans = int(v * 10 ** n + 0.5) / 10 ** n
    print(ans)
main()