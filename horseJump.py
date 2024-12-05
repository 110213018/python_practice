]9# 姓名: 陳宣閔
# 學號: 110213018
def main():
    n, m = map(int,input().split())  # 表示莊園大小
    data = [[ col for col in input().split() ] for row in range(m) ] # 輸入莊園資料
    r, c = map(int,input().split())  #馬的起始位置
    print(findAns(n, m, data, r, c))

def findAns(n, m, data, r, c):
    maxLen = 0 # 紀錄最大的長度
    data[r][c] = '1'
    # ro = -2, -2, -1, -1,  1, 1,  2, 2    CF: 1=下, -1=上, 2=下下, -2=上上
    # co = -1,  1, -2,  2, -2, 2, -1, 1   CF: 1=右, -1=左, 2=右右, -2=左左
    # 左上上、右上上、左左上、右右上、左左下、右右下、左下下、右下下
    for ro,co in [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]:
        # 0<=r+ro<m : 跳下去的位置(列)不能超過or小於m的長度
        # 0<=c+co<n : 跳下去的位置(行)不能超過or小於n的長度
        # data[r+ro][c+co]!='1' : 跳過去的位置不能為'1'(有馬)
        if 0<=r+ro and r+ro<m and 0<=c+co and c+co<n and data[r+ro][c+co]!='1':
            data[r+ro][c+co] = '1'
            thisLen = 1 + findAns(n, m, data, r+ro, c+co)
            # 跑完一個結果之後, 開始一步一步復原
            # 每回復一步, tL+1, 直到回復到有新路線可以走, 再開始計算新的tL
            if maxLen < thisLen: # 如果現在測的長度大於之前測的長度就交換
                maxLen = thisLen
            data[r+ro][c+co] = '0'  # 將第16列改過的位置, 復原為'0'
    return maxLen  # 回傳到21列, 全部結果都比較完之後, 回傳至第7列

main()