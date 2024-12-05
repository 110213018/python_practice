# 陳宣閔
# 110213018
def main():
    import random
    x = 10 # 隨機選出長度
    data = []
    for i in range(x): # 在-100~100，隨機選出x個數字
        data.append(random.randint(-100,100))
    print("學號:110213018，姓名:陳宣閔")
    print("原始資料：",data) # 輸出每一輪的結果
    ans = []
    for i in range(len(data)):
        if (len(ans)!=x):
            findMin(data, ans)
        else:
            break
    print("最小值：",ans[0])

def findMin(data, ans):
    minNum = min(data)
    data.remove(minNum)
    ans.append(minNum)
    return ans
main()