import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[0] * n for i in range(n)]

# 지도 만들기
for i in range(n):
    row = sys.stdin.readline()    
    for j in range(n):
        matrix[i][j] = int(row[j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count_arr = []
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    matrix[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            count_arr.append(bfs(i,j))

count_arr.sort()

print(len(count_arr))

for i in count_arr:
    print(i)