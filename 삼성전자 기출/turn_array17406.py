from collections import deque
from itertools import permutations

n, m, k = map(int, input().split())

answer = []

matrix = []
turn_list = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(k):
    turn_list.append(list(map(int, input().split())))

turn_list = list(permutations(turn_list, k))

visited = []

for i in range(n):
    temp_arr = []
    for j in range(m):
        temp_arr.append(0)
    visited.append(temp_arr)

for turn in turn_list:
        
    status = ""
    for a in range(k):
        visited = []
        for i in range(n):
            temp_arr = []
            for j in range(m):
                temp_arr.append(0)
            visited.append(temp_arr)
        r = turn[a][0]
        c = turn[a][1]
        s = turn[a][2]
        x1 = r - s - 1
        y1 = c - s - 1
        x2 = r + s - 1
        y2 = c + s - 1
        temp_deque = deque()
        temp_deque.append(matrix[x1][y1])
        visited[x1][y1] = 1
        temp = matrix[x1][y1]
        i = x1
        j = y1 + 1
        status = "right"
        while temp_deque:
            if visited[i][j] == 1:
                temp_deque.pop()
            else:
                visited[i][j] = 1
            if status == "right":    
                if x1 == i and j < y2:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    j += 1
                else:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    status = "down"
                    i += 1
            elif status == "down":
                if x2 > i and j == y2:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    i += 1
                else:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    j -= 1
                    status = "left"
            elif status == "left":
                if y1 < j and i == x2:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    j -= 1
                else:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    i -= 1
                    status == "up"
            elif status == "up":
                if x1 == j and i > x1:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    i -= 1
                else:
                    temp_deque.append(matrix[i][j])
                    matrix[i][j] = temp_deque.popleft()
                    i -= 1
            if i == x1 and j == y1:
                #여기서 바꾸기 실행
                matrix[x1][y1] = temp_deque.popleft()
                
                x1 = x1 + 1
                y1 = y1 + 1
                x2 = x2 - 1
                y2 = y2 - 1
                if x1 == x2 and y1 == y2:
                    break
                i = x1
                j = y1 + 1
                status = "right"
                temp_deque.append(matrix[x1][y1])
                visited[x1][y1] = 1
            #여기부터 돌리는 걸 한번 했을 때

    temp_answer = []
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += matrix[i][j]
        temp_answer.append(sum)
    answer.append(min(temp_answer))
                    
                
print(min(answer))
            
    