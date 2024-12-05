def main():
    a = 'cutString' # 字串"" ''都可
    for i in range(len(a)):
        print(a[i],i) # 輸出字母+其對應的位置
    b = '1 2 3 4'
    print(b.split())
main()

'''
split:

txt = "a#b#c"
x = txt.split("#", 1)
print x
-->['a', 'b#c']

 '1 2 33 55 7'.split()    --> ['1' , '2' , '33', '55', '7']
 '1,2,3,4'.split()        --> ['1,', '2,', '3,', '4,']
 '1,2,3,4'.split(',') --> ['1' , '2' , '3' ,  '4']

'''

'''
 list : 語法 [起始 : 終止 : 迭代(間格)]
 索引值是從零開始算,
 [-1:-4] 會跑不出東西，要告訴它怎麼迭代。例如: [-1, -4, -2]

 'abcdef'[4]        --> 'e'
 'abcdef'[0]        --> 'a'
 'abcdef'[8]        --> string index out of range  #超出範圍
 'abcdef'[0:3]      --> 'abc'  #拿第0個~第2個
 'abcdef'[0:5:2]    --> 'ace'  #拿第0個~第4個,間隔2個拿
 'abcdef'[-1]       --> 'f'  #拿倒數第一個
 'abcdef'[-1:-4]    --> ''
 'abcdef'[-1:-4:-1] --> 'fed'
 'abcdef'[::-1]     --> 'fedcba'

'''