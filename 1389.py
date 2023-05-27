import sys
from collections import deque

n ,m = map(int, sys.stdin.readline().split())

matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
def bfs(a):
    queue = deque()
    queue.append(a)
    
    while queue:
        node = queue.popleft()
        for i in matrix[node]:
            if visited[i] == 0 and i != a:
                queue.append(i)
                visited[i] = visited[node] + 1
    return visited

answers = []
for i in range(1,n+1):
    visited = [0] * (n+1)
    sum = 0
    for j in bfs(i):
        sum += j
    answers.append(sum)
temp = n * n
answer = 0
for i in range(len(answers)):
    if answers[i] < temp:
        answer = i+1
        temp = answers[i]
    
print(answer)