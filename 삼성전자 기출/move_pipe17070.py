n = int(input())
graph = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우
        if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]


def dfs(x,y, direction):
    
    global count
    
    if x < 0 or y < 0 or x >= n - 1 or y >= n - 1:
        return
    if matrix[x][y] == 1:
        count -= 1
        return
    elif x == n - 1  and y == n - 1:
        count += 1
        return
    else:
        if direction == 'width':
            operator('width', x, y)
        elif direction == 'height':
            operator('height', x, y)
        else:
            operator('diagonal', x, y)

dfs(0,1, 'width')
print(count)
