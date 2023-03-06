import sys
from collections import deque

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

matrix = [[0] * (n+1) for i in range(n+1) ]
visited = [0 for i in range(n+1)]

#dfs 문제
def dfs(v):
    visited[v] = 1 

    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            visited[i] = 1
            dfs(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
dfs(1)
answer = 0
for i in visited:
    if i == 1:
        answer +=1
print(answer -1)
