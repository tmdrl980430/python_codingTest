import sys

n = int(input())

matrix = []

count = 0

for i in range(n):
    temp_list = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp_list)


def operator(move, x, y):

    if move == 'width': #가로
        print('가로')
        dfs(x + 1, y+1, 'diagonal')
        dfs(x + 1, y, 'width')
    elif move == 'height': #세로
        print('세로')
        dfs(x + 1, y+1, 'diagonal')
        dfs(x, y + 1, 'height')
    else: #대각선 (diagonal)
        print('대각선')
        dfs(x + 1, y+1, 'diagonal')
        dfs(x, y + 1)
        dfs(x + 1, y)


def dfs(x,y, direction):
    global count
    
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    if matrix[x][y] == 1 or x < 0 or y < 0 or x >= n or y >= n:
        return
    elif x == n and y == n:
        return count
    else:
        if direction == 'width':
            operator('width', x, y)
            count += 1 
        elif direction == 'height':
            operator('height', x, y)
            count += 1
        else:
            operator('diagonal', x, y)
            count += 1

print(dfs(0,1, 'width'))