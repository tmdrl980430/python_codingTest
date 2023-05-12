import sys
from collections import deque

m , n , k  = map(int, sys.stdin.readline().split())

matrix = [[0] * n for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


#matrix 생성

for i in range(k):
    temp = list(map(int, sys.stdin.readline().split()))
    for a in range(temp[1], temp[3]):
        
        for j in range(temp[0],temp[2]):
            matrix[a][j] = 1

result = []

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    matrix[a][b] = 1
    count = 1
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if matrix[nx][ny] == 0:
                queue.append((nx,ny))                    
                matrix[nx][ny] = 1
                count += 1
    return count

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i], end=' ')