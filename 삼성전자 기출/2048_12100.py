n = int(input())

matrix = []
for i in range(n):
    temp_arr = list(map(int, input().split()))
    matrix.append(temp_arr)

count = 0
dx = [1,-1,0,0]
dy = [0,0,-1,0]

def operator(oper):
    if oper == "up":
        for i in range(n):

