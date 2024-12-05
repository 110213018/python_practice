#學號:110213018
#姓名:陳宣閔
def main():
    Find_Odd_Even(list(map(int,input().split())))#輸入一列表,並分割元素.
    
#算出奇數偶數之總和
def Find_Odd_Even(number):
    even=0
    odd=0
    for i in number:
        if i%2==0:   #如果除2的餘式為0,他就是偶數.
            even+=i  #算出偶數總和.
        else:        #如果除2的餘式不為0,他就是奇數.
            odd+=i   #算出奇數總和.
    print(odd, even) #輸出奇數偶數,並在兩數之間加一個空白鍵.

main()