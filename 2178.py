import sys
from collections import deque

n , m = map(int, sys.stdin.readline().split())

    # 방향벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = [[0] * m for i in range(n)]


for i in range(n):
    mat = input()
    for j in range(m):
        matrix[i][j] = int(mat[j])

def bfs(x ,y):
    queue = deque([(x, y)])
    while queue:
        x , y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] += matrix[x][y]
    return matrix[n - 1][m -1]


print(bfs(0,0))   