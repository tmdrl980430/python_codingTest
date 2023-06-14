# 로봇 청소기
# 시뮬레이션 문제

# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램

# 로봇 청소기 작동 방식
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    # 2-1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    # 2-2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    # 3-1 반시계 방향으로 90도 회전한다.
    # 3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진한다.
    # 3-3 1번으로 돌아간다.
import sys
from collections import deque

input = sys.stdin.readline
N , M = map(int, input().split())

matrix = []

r, c, d = map(int, input().split())

dx = [0 ,1, 0, -1]
dy = [1, 0, -1 , 0]
# 동 북 서 남

visited = [[False] * N for _ in range(M)]

for i in range(N):
    temp =list(map(int, input().split()))
    matrix.append(temp)

answer = 0
# 반시계 방향으로 회전한다 ===> 동 -> 북 -> 서 -> 남 -> 동 이런식으로 회전한다는 말

def clear(x ,y):
    global d, answer, visited, matrix
    #현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소한다.
    if visited[x][y] == False and matrix[x][y] == 0:
        visited[x][y] = True
        answer += 1
        return x, y
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    for i in range(4): #주변 4칸에 청소되지 않은 빈 칸이 있는지 없는지 판별만 하기;
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or  ny < 0 or nx >= N or ny >= M:
            continue
        if matrix[nx][ny] == 0:
            a, b = third_clear(x, y)# 주변 4칸중에 빈칸이면서 청소가 안되어 있으면 queue 삽입
            if a == x and b == y:
                continue 

    a, b = second_clear(x,y)
    if a == -1 and b == -1:
        return -1,-1
    
    return x, y

def second_clear(x,y):
    global d
    #바라보는 방향을 유지한 채로 한칸 후진할 수 있다면 후진하고 1번으로 돌아감
    if matrix[x - dx[d]][y - dy[d]] == 0:
        # 후진할 수 있다면
        x = x - dx[d]
        y = y - dy[d]
        #후진하고
        #1번으로 돌아감
        return x, y
    else:
        return -1,-1



def third_clear(x,y) :
    global d
    d += 1
    if d  == 4:
        d = 0
    ax = x + dx[d]
    ay = y + dy[d]
    if ax < 0 or  ay < 0 or ax >= N or ay >= M:
        return x , y
    if matrix[ax][ay] == 0 and visited[ax][ay] == False:
        return ax, ay #전진한 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다. 그리고 1번으로 돌아감
    elif matrix[ax][ay] == 0 and visited[ax][ay] == True:
        return x , y # 전진한 칸이 청소가 되어 있으면 그냥 1번으로 돌아감

while True:
    
    answer1, answer2 = clear(r,c)
    if answer1 == -1 and answer2 == -1:
        break

print(answer)