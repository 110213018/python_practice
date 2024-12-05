# 陳宣閔
# 110213018
def main():
    import random
    x = random.randint(10, 20) # 隨機選出長度
    data = []
    for i in range(x): # 在-50~50，隨機選出x個數字
        data.append(random.randint(-50,50))
    for i in range(x-1): # 換幾輪
        for j in range(x-1): # 一輪換幾次
            if data[j] > data[j+1]: # 如果前面數字比後面大，就交換位置
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
        print(data) # 輸出每一輪的結果
main()