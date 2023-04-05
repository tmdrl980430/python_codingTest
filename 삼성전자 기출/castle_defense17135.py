n, m, d = map(int, input().split())

matrix = []

for i in range(n):
    temp_arr = list(map(int, input().split()))
    matrix.append(temp_arr)

print(matrix)