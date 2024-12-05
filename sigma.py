def main():
    n=int(input())
    sum = 0
    for k in range(1,n+1):
        sum += ((2*k)-1)/(k*(k+1)*(k+2))
    print(sum)
main()