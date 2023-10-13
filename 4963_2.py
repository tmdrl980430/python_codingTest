from collections import deque
#한 곳에 들어가서  주변을을 다 살펴보고 이어져 있으면 0을 만들고 그 주변도 살펴보는 것
#이렇게 찾아서 한가지 섬을 찾고 나오면 count를 올려주면 한가지 섬의 개수를 출력함

dx = [0 ,0 ,1 ,-1, 1, -1, 1, -1]
dy = [1, -1 , 0, 0, 1, -1, -1, 1]

answers = []
def bfs(a,b):
    queue = deque([(a,b)])
    
    while queue:
        x , y = queue.popleft()
        
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    count = 0
    if w == 0 and h == 0:
        break
    
    matrix = []
    
    for i in range(h):
        temp = list(map(int, input().split()))
        matrix.append(temp)

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i,j)
                count += 1
    answers.append(count)
print(answers)

