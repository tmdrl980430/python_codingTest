import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


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
            if 0 > nx or 0 > ny or m <= nx or n <= ny:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))
        count += 1
    return count

count_arr = []

for a in range(t):
    m , n , k = map(int, sys.stdin.readline().split())
    count_arr = []
    matrix = [[0] * (n) for x in range(m)]
    for i in range(k):
        g,h = map(int, sys.stdin.readline().split())
        matrix[g][h] = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                count_arr.append(bfs(i,j))
    print(len(count_arr))
