# 姓名:陳宣閔
# 學號:110213018
#python addMagic.py

# pos: the position i have to fill
# s: string of a,b,c
# la,lb,lc: length of a,b,c
#1??2 ?442 7?44
def main():
    a,b,c=input().split()
    findsol(a+b+c,len(a),len(b),len(c),0)

def findsol(s,la,lb,lc,pos):
    #如果問號都變數字了,就找出符合a+b=c的數列
    if len(s)==pos:
        if fitEq(s,la,lb,lc):
            print(s[0:la],s[la:la+lb],s[la+lb:])
        return
    #在s中找出問號,並用str(i)取代問號
    if s[pos]=='?':
        for i in range(10):
            findsol(s[:pos]+str(i)+s[pos+1:],la,lb,lc,pos+1)
    #如果已有數字,就不用再處理
    else:
        findsol(s,la,lb,lc,pos+1)
        
#找出符合a+b=c的數列
def fitEq(s,la,lb,lc):
    return int(s[0:la])+int(s[la:la+lb])==int(s[la+lb:])
    
main()