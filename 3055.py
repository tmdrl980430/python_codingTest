from collections import deque


r, c = map(int, input().split())

matrix = [[''] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
distance = [[0] * c for _ in range(r)]
D_space = [0,0]
S_space = [0,0]
for i in range(r):
    temp = input()
    for j in  range(c):
        if temp[j] == 'S':
            D_space[0] = i
            D_space[1] = j
            continue
        elif temp[j] == 'D':
            S_space[0] = i
            S_space[1] = j

        matrix[i][j] = temp[j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def fill_water():
    temp = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '*':
                #주변부에 채울공간 저장하기
                for a in range(4):
                    di = i + dx[a]
                    dj = j + dy[a]
                    if di < 0 or dj < 0 or di >= r or dj >= c:
                        continue
                    if matrix[di][dj] == '*':
                        continue
                    elif matrix[di][dj] != 'D' or matrix[di][dj] != 'X':
                        # 물이 찰 예정에 고슴도치의 위치 고려해야함
                        if temp not in (di, dj):
                            temp.append((di,dj))
    for i in temp:
        if matrix[i[0]][i[1]] == 'X' or matrix[i[0]][i[1]] == 'D':
            continue
        if matrix[i[0]][i[1]] == 'S':
            return False
        matrix[i[0]][i[1]] = '*'
        

def bfs(a, b):
    q = deque()
    visited[a][b] = True
    q.append((a,b))
    while q:
        if fill_water() == False:
            break
        x, y  = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if matrix[nx][ny] == 'D':
                #끝
                distance[nx][ny] = distance[x][y] + 1
                return distance[nx][ny]
            if matrix[nx][ny] != '*' and matrix[nx][ny] != 'X' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
            else:
                continue
    return -1

if D_space == S_space:
    print(0)
else:    
    result = bfs(D_space[0], D_space[1])
    if result == -1:
        print("KAKTUS")
    else:
        print(result)