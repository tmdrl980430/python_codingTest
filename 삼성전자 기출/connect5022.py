from collections import deque
import heapq
INF = int(1e9)
n ,m = map(int, input().split())

A = []
B = []

matrix = []
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 0]

for i in range(n):
    temp_arr = []
    for j in range(m):
        temp_arr.append(0)
    matrix.append(temp_arr)
    visited.append(temp_arr)

#A, B 입력
for i in range(4):
    if i < 2:
        A.append(list(map(int, input().split())))
    else:
        B.append(list(map(int, input().split())))

#선 만드는 함수
dist = 0
def bfs(x,y):
    queue = deque([(x[0], x[1])])
    while queue:
        a , b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                queue.append((nx,ny))
                matrix[nx][ny] += matrix[a][b]
            if nx == y[0] and ny == y[1]:
                
                return
    return matrix[n - 1][m -1]


distanse_A = abs(A[0][0] - A[1][0]) + abs(A[0][1] - A[1][1])
distanse_B = abs(B[0][0] - B[1][0]) + abs(B[0][1] - B[1][1])
bfs(A[0], A[1])
print(matrix[A[1][0]][A[1][1]])
print(matrix[B[1][0]][B[1][1]])

print(distanse_A)
print(distanse_B)

