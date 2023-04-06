import sys

n = int(input())

matrix = []

count = 0

for i in range(n):
    temp_list = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp_list)


def operator(move, x, y):

    if move == 'width': #가로
        dfs(x + 1, y+1, 'diagonal')
        dfs(x + 1, y, 'width')
    elif move == 'height': #세로
        dfs(x + 1, y+1, 'diagonal')
        dfs(x, y + 1, 'height')
    else: #대각선 (diagonal)
        dfs(x + 1, y+1, 'diagonal')
        dfs(x, y + 1, 'height')
        dfs(x + 1, y, 'width')


def dfs(x,y, direction):
    
    global count
    
    if x < 0 or y < 0 or x >= n - 1 or y >= n - 1:
        return
    if matrix[x][y] == 1:
        count -= 1
        return
    elif x == n - 1  and y == n - 1:
        count += 1
        return
    else:
        if direction == 'width':
            operator('width', x, y)
        elif direction == 'height':
            operator('height', x, y)
        else:
            operator('diagonal', x, y)

dfs(0,1, 'width')
print(count)