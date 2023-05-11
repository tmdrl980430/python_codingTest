import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

matrix = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(n -1):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)

def dfs(a):
    for i in matrix[a]:
        if visited[i] == 0:
            visited[i] = a
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])