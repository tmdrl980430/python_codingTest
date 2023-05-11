import sys
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

w = 0
h = 0
matrix = []


def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x , y = queue.popleft()
        
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))
    
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    count = 0
    matrix = []
    visited = []
    
    for i in range(h):
        temp = list(map(int, sys.stdin.readline().split()))
        matrix.append(temp)
        temp_visited = []
        for j in range(w):
            temp_visited.append(False)
        visited.append(temp_visited)
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i,j)
                count += 1
    
    print(count)
    
    