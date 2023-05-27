import sys
from collections import deque


n = int(sys.stdin.readline())

a,b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)

def bfs(c):
    queue = deque()
    queue.append(c)
    
    
    while queue:
        d = queue.popleft()
        for i in matrix[d]:
            if visited[i] == 0 and i != a:
                queue.append(i)
                visited[i] = visited[d] + 1
 
        
bfs(a)

answer = -1
if visited[b] != 0:
    answer = visited[b]

print(answer)    