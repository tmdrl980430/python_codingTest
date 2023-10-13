from collections import deque


n , m = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

matrix = [[0]* m for _ in range(n)]
for i in range(n):
    temp = input()
    for j in range(m):
        matrix[i][j] = int(temp[j])

def bfs (a,b):
    count = -1
    queue = deque([(a,b)])
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] += matrix[x][y]
    return matrix[n-1][m-1]

print(bfs(0,0))