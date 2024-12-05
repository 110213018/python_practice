#學號:110213018
#姓名:陳宣閔
def main():
     #求ax^2+bx+c
     #a,b,c為三邊長.打float是因為輸入數字有小數點
     a=float(input())
     b=float(input())
     c=float(input())
     s=(a+b+c)/2     
     print((s*(s-a)*(s-b)*(s-c))**0.5) #輸出命令
     
main()