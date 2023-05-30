import sys
from collections import deque

n , m = map(int, sys.stdin.readline().split())

matrix = [[] * m for _ in range(n)]

blue_x = 0
blue_y = 0

red_x = 0
red_y = 0

hole_x = 0
hole_y = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    temp = sys.stdin.readline()
    for j in range(m):
        matrix[i].append(temp[j])
        if temp[j] == "B":
            blue_x = i
            blue_y = j
        elif temp[j] == "R":
            red_x = i
            red_y = j
        elif temp[j] == "O":
            hole_x = i
            hole_y = j

def bfs(a ,b , c, d):
    queue = deque()
    queue.append((a,b,c,d))
    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((a, b, c, d))
    count = 0
    while queue:
        for _ in range(len(queue)):
            
            rx , ry , bx, by = queue.popleft()
            
            if count > 10:
                print(-1)
                return
            if matrix[rx][ry] == 'O':
                print(count)
                return
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if nrx < 0 or nry < 0 or nrx >= n or nry >= m:
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if matrix[nrx][nry] == "#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if matrix[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if nbx < 0 or nby < 0 or nbx >= n or nby >= m:
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if matrix[nbx][nby] == "#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if matrix[nbx][nby] == 'O':
                        break
                if nbx < 0 or nby < 0 or nbx >= n or nby >= m or nrx < 0 or nry < 0 or nrx >= n or nry >= m:
                    continue
                elif matrix[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append(((nrx, nry, nbx, nby)))
        count += 1
    print(-1)
bfs(red_x, red_y, blue_x, blue_y)
                
                
                
                
