m = int(input("row: "))
n = int(input("column: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(m):
    for j in range(n):
        print(f"{matrix[i][j]}", end=" ")
    print()

for i in range(m):
    sum = 0
    for j in range(n):
        sum += matrix[i][j]
    if(sum % 2 != 0):
        print(f"Dòng {i} (tổng : {sum})")
