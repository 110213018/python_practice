# 姓名:陳宣閔
# 學號:110213018

# p%9 vertical line(小column), p//9 horizontal line(小row)
# 小row//3 ==> 大row, 小column//3 ==> 大column, 大row*3+大column ==> block編號, p//9//3*3+p%9//3 block?
# xxx
# xxx p//3*3+p%3
# xxx

def findSol(color, puz):
    r=[[True for i in range(9)]for j in range(9)]  # 列
    c=[[True for i in range(9)]for j in range(9)]  # 行
    b=[[True for i in range(9)]for j in range(9)]  # 九宮格中的九個小宮格
    for p in range(81):
        if puz[p] != 0:  # 如果這個位置不是0,就等於False
            r[p//9][puz[p]-1],c[p%9][puz[p]-1],b[color[p]][puz[p]-1] = False, False, False
    fillPuzzle(color, puz, r, c, b, 0)

# puz: puzzle data, 0 for free, 1~9 fixed
# r:   list for 9 booleans, represent which number can be filled in this row
# c:   list for 9 booleans, represent which number can be filled in this column
# b:   list for 9 booleans, represent which number can be filled in this block
# pos: which position I am responsible to fill

def fillPuzzle(color, puz, r, c, b, p):
    if p == 81:  # 如果81個位置都跑過一遍的話,就輸出完成後的數獨版面,9個一排
        for i in range(81):
            print(puz[i],end='')
            if i%9==8:  # 到了每一列的最後一個數字就換列
                print()
        return
    if puz[p] != 0:  # 如果已經填過數字,就跑下一個位置
        fillPuzzle(color, puz, r, c, b, p+1)
        return
    for d in range(9):  # 填數字在True的位置
        if r[p//9][d] and c[p%9][d] and b[color[p]][d]:
            puz[p] = d+1  # 填入數字(1~9)
            r[p//9][d], c[p%9][d], b[color[p]][d] = False, False, False  # 填過數字的話,就變成False
            fillPuzzle(color, puz, r, c, b, p+1)# 如果已經填過數字,就跑下一個位置
            puz[p] = 0
            r[p//9][d], c[p%9][d], b[color[p]][d] = True, True, True  # 復原

def main():
    color = list(map(int,input()))  # 輸入數字,每個不同的數字都代表不同顏色
    puz = list(map(int,input()))  # 數獨上存在的數字,0代表此格為空格
    findSol(color,puz)

main()