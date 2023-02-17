import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
m,n = map(int, sys.stdin.readline().split())

matrix = [[0] * m for i in range(n)]
for i in range(n):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

def bfs():
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if ny < 0 or nx < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
            elif matrix[nx][ny] == -1:
                continue
                
all_taste = True
is_no = False

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append((i,j))
        elif matrix[i][j] == 0:
            all_taste = False
            
bfs()
temp = 0
for i in range(n):
    for j in range(m):
        if temp < matrix[i][j]:
            temp = matrix[i][j]
        if matrix[i][j] == 0:
            is_no = True
            


if all_taste:
    print(0)
elif is_no:
    print(-1)
else:
    print(temp - 1)