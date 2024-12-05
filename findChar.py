#學號:110213018
#姓名:陳宣閔

#輸入兩個串列
def main():
    Eng1=list(map(str,input()))
    Eng2=list(map(str,input()))
    Find_same(Eng1,Eng2)

#找出相同字母並印出其位置
def Find_same(Eng1,Eng2):
    same=[] #建立一個空串列
    for i in range(len(Eng1)):
        for j in range(len(Eng2)):
            if Eng1[i]==Eng2[j]:
                same.append(i) #將相同字母的位置嵌入空串列
    print(*same)
main()