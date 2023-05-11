import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

matrix = [[] for _ in range(n + 1)]

visited = [False] * (n+1)

for i in range(m):
    x ,y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for i in matrix[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
result = 0 
for i in range(1,n+1):
    if not visited[i]:
        if not matrix[i]:
            result+=1
            visited[i] = True
        else:
            bfs(i)
            result += 1
            
        
    

print(result)