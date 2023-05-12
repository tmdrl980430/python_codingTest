import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

matrix = []
dx = [0,0,-1,1]
dy = [1, -1,0,0]

dp = [[-1] * n for _ in range(m)]

for i in range(m):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp_arr)



def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        elif matrix[x][y] > matrix[nx][ny]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))