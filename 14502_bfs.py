import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())

matrix = [[0] * m for i in range(n)]
count = 0
result = 0
for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    matrix[i] = temp_arr
#콤비네이션으로 벽3개를 세우고 바이러스를 퍼뜨리고 0의 개수를 찾는다. ->> 시간 초과 날 것 같음
def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                make_wall(count + 1)
                matrix[i][j] = 0
                
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count_arr = []
def bfs():
    queue = deque()
    test_matrix = copy.deepcopy(matrix)
    for i in  range(n):
        for j in  range(m):
            if test_matrix[i][j] == 2:
                queue.append((i,j))
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if test_matrix[nx][ny] == 0:
                    test_matrix[nx][ny] = 2
                    queue.append((nx,ny))
    global result
    count = 0
    for  i in range(n):
        for j in range(m):
            if test_matrix[i][j] == 0:
                count += 1
    result = max(result, count)

make_wall(0)
print(result)
