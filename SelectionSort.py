def main():
    import random
    x = 10 # 長度10
    data = []
    for i in range(x): # 在-50~50，隨機選出x個數字
        data.append(random.randint(-50,50))
    print("原始資料","\n",data)
    findAns(data)

def findAns(data):
    
main()