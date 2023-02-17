import sys
from collections import deque

n , m , v = map(int, sys.stdin.readline().split())

arr = []

matrix = [[0] * (n+1) for i in range(n+1)]

visited = [0] * (n+1)

for i in range(m):
    m_arr = list(map(int, sys.stdin.readline().split()))
    matrix[m_arr[0]][m_arr[1]] = 1
    matrix[m_arr[1]][m_arr[0]] = 1

def dfs(v):
    visited[v] = 1 
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 1 and matrix[v][i] == 1:
            dfs(i)

    
def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0
        
    
dfs(v)
print()
bfs(v)