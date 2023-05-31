from collections import deque

# 이동 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 구슬 이동 함수
def move(x, y, dx, dy):
    count = 0
    # 다음 위치로 이동할 수 있을 때까지 이동
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

# BFS 탐색 함수
def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited = set([(rx, ry, bx, by)])
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        
        # 최대 10번 이동까지만 확인
        if depth > 10:
            break
        
        # 4가지 이동 방향에 대해
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            # 파란 구슬이 구멍에 빠졌을 경우는 실패이므로 다음 방향 확인
            if board[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬이 구멍에 빠졌을 경우는 성공이므로 결과 반환
            if board[nrx][nry] == 'O':
                return depth
            
            # 빨간 구슬과 파란 구슬이 겹칠 경우 위치 조정
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            # 이전에 방문한 상태가 아니라면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                queue.append((nrx, nry, nbx, nby, depth + 1))
                visited.add((nrx, nry, nbx, nby))
    
    # 실패일 경우 -1 반환
    return -1


# 입력 처리
n, m = map(int, input().split())
board = []
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    row = list(input().strip())
    board.append(row)
    if 'R' in row:
        rx, ry = i, row.index('R')
    if 'B' in row:
        bx, by = i, row.index('B')

# BFS 탐색 실행
result = bfs(rx, ry, bx, by)

# 결과 출력
print(result)
