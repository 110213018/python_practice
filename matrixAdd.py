def main():
    print(add([[1,2],[3,4]],[[5,6],[7,8]]))

def add(A, B):
    result = []
    for r in range(len(A)):
        row=[]
        for c in range(len(A[0])):
            row.append(A[r][c]+B[r][c])
        result.append(row)
    return result

main()