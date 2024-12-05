#學號:110213018
#姓名:陳宣閔
def main():
    a=int(input()) #輸入第一個整數
    b=int(input()) #輸入第二個整數
    c=int(input()) #輸入第三個整數
    list1=sorted([a,b,c]) #打sorted是為了排出由小到大的數列
    x=list1[0] #取出數列中的第一個元素
    y=list1[1] #取出數列中的第二個元素
    z=list1[2] #取出數列中的第三個元素
    print(x,y,z) #輸出,且數字間有一個空白間格，最後一個數字後無空白
    if((x+y)<z): #最小的兩個邊長相加如果小於最長邊,則無法變成三角形
        print('No')
    elif((x**2+y**2)==z**2):#最小的兩個邊長平方相加如果等於最長邊平方,則出現直角三角形
        print('Right')
    elif((x**2+y**2)>z**2):#最小的兩個邊長平方相加如果大於最長邊平方,則出現銳角三角形
        print('Acute')
    else:#上述執行都是false,則出現鈍角三角形
        print('Obtuse')

main()