import sys
from collections import deque
#Dummy 라는 도스게임
# 뱀이 나와서 기어다니는 게임인데 사과를 먹으면 뱀 길이가 늘어난다.
# 벽 또는 자신의 몸에 부딪히면 게임 끝

# N * N  정사각형의 맵

n = int(sys.stdin.readline())
apple_count = int(sys.stdin.readline())

# 뱀이 있는 곳은 1, 사과가 있는 곳은 2, 아무것도 없는 곳은 0으로 설정한다.
matrix = [[0] * n for _ in range(n)]

# 사과의 위치 추가
for i in range(apple_count):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x- 1][y-1] = 2

matrix[0][0] = 1 #뱀의 위치 추가
L = int(sys.stdin.readline())

move_count = [] # 방향전환 횟수 배열
move_directions = [] #회전 방향 배열

#방향 관련 정보 입력
for i in range(L):
    c, direction = map(str, sys.stdin.readline().split())
    move_count.append(int(c))
    move_directions.append(direction)

dx = [-1, 0 , 1 , 0]
dy = [0, 1, 0, -1]
#상우하좌 시계방향
current_direction = 1 # 초기 방향은 오른쪽

def rotate(direction , current_direction_index):
    global current_direction
    if direction == 'D':
        if current_direction_index == 3:
            current_direction = 0
        else:
            current_direction += 1
        # 오른쪽으로 90도 회전
        
    else:
        # 왼쪽으로 90도 회전
        if current_direction_index == 0:
            current_direction = 3
        else:
            current_direction -= 1

def move(head_x, head_y):
    # 현재 머리와 꼬리의 위치, 방향을 입력받고 한칸 이동
    global current_direction
    head_x += dx[current_direction]
    head_y += dy[current_direction]
    if head_x >= n or head_y >= n or head_x < 0 or head_y < 0:
        #벽에 부딪히면 게임끝
        return (n, n)
    if matrix[head_x][head_y] == 2: #사과가 있으면 길이가 늘어남
        matrix[head_x][head_y] = 1
        # 꼬리가 그대로여야 함
    elif matrix[head_x][head_y] == 1: #자신에게 부딪혀서 게임 끝
        return (n, n)
    elif matrix[head_x][head_y] == 0:
        #꼬리가 사라져야 함
        matrix[head_x][head_y] = 1
        tail_x, tail_y = find_tali(head_x, head_y)
        matrix[tail_x][tail_y] = 0
    return (head_x, head_y)

def find_tali(x , y): # 머리의 위치를 인자로 받고 bfs 탐색으로 꼬리의 위치를 찾아냄
    queue = deque()
    queue.append((x,y))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    tail_x = x
    tail_y = y
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                tail_x = nx
                tail_y = ny
    
    return [tail_x, tail_y]
answer = 0
rotate_count = 0

x = 0
y = 0
while True:
    x, y = move(x, y)
    answer += 1
    if answer ==  move_count[rotate_count]:
        rotate(move_directions[rotate_count], current_direction)
        rotate_count += 1
        if rotate_count == len(move_count):
            rotate_count = 0 
    if x == n and y == n:
        print(answer)
        break