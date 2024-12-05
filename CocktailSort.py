# 陳宣閔
# 110213018
def main():
    import random
    x = random.randint(10, 20) # 隨機選出長度
    data = []
    for i in range(x): # 在-50~50，隨機選出x個數字
        data.append(random.randint(-50,50))
    print(data)
    for i in range(x-1): # 換幾輪
        for j in range(x-1): # 一輪換幾次
            if data[j] > data[j+1]: # 如果前面數字比後面大，就交換位置
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
        for v in range(x-1,0,-1): # 一輪換幾次
            if data[v] < data[v-1]: # 如果後面數字比前面小，就交換位置
                temp = data[v]
                data[v] = data[v-1]
                data[v-1] = temp
        print(data)
        check = 0
        for z in range(x-1): # 一輪換幾次
            if data[z] < data[z+1]:
                check+=1
                if check == x-1:
                    exit() # 如果結果為小到大就結束程式
main()