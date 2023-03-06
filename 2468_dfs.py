import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[0] * n for i in range(n)]

max_n = 0

for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp_arr[j] >= max_n:
            max_n = temp_arr[j]
    matrix[i] = temp_arr

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count_arr = []
def bfs(x, y, z, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            if matrix[nx][ny] > z and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                count += 1
    return count
result = 0
for z in range(max_n):
    visited = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and matrix[i][j] > z:
                count_arr.append(bfs(i,j,z,visited))
                
    if result <= len(count_arr):
        result = len(count_arr)
    count_arr = []
print(result)