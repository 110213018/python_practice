def main():
    n = int(input())
    line = 1
    while line<=n:
        print('*'*line)
        line += 1
    # 4
    # *
    # **
    # ***
    # ****
main()

def main():
    n = int(input())
    line = 1
    while line<=n:
        print(' '*(n-line)+'*'*(line*2-1))
        line+=1
    # 4
    #     *
    #    ***
    #   *****
    #  *******
main()

def main():
    n = int(input())
    line = 1
    while line<=n:
        print(' '*(n-line)+'*'*(line*2-1))
        line+=1
    line = n-1 # 倒數第幾行(不管之前的line，重新訂一個數)
    while line>=1:
        print(' '*(n-line)+'*'*(line*2-1))
        line-=1
    # 4
    #     *
    #    ***
    #   *****
    #  *******
    #   *****
    #    ***
    #     *
main()