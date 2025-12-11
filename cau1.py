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

# for i in range(m):
#     curr_sum = 0
#     for j in range(n):
#         curr_sum += matrix[i][j]
#     if(curr_sum % 2 != 0):
#         print(f"Dòng {i} (tổng : {curr_sum})")
# cach 2:

for i in range(m):
    row_sum = sum(matrix[i])

    if(row_sum % 2 != 0):
        print(f"Dòng {i} (tổng : {row_sum})")
