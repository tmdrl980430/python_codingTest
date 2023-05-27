import sys
from collections import deque

N, L , R = map(int, sys.stdin.readline().split())

matrix = [] 
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
open = []

def open_bfs():
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            
            if nx >= 0 and ny >= 0 and nx < N and ny < N and  open[nx][ny] == False:

                queue.append((nx,ny))
                if L <= abs(matrix[nx][ny] - matrix[x][y]) <= R:
                    open[nx][ny] = True
                    open[x][y] = True
answer = 0
while True:
    answer += 1
    sum = 0
    count = 0
    temp = []
    open = [[False]*N for _ in range(N)]
    open_bfs()
    for i in range(N):
        for j in range(N):
            if open[i][j] == True:
                temp.append((i,j))
                sum += matrix[i][j]
                count += 1
            else:
                continue
    if count == (N*N):
        break
    for i in range(count):
        a, b = map(temp[i])
        matrix[a][b] = sum // count
print(answer) 
    