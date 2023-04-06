from itertools import combinations
import copy

n, m, d = map(int, input().split())

matrix = []
temp_answer = 0
answer = 0
arr = []

for i in range(n):
    temp_arr = list(map(int, input().split()))
    matrix.append(copy.deepcopy(temp_arr))

for i in range(m):
    arr.append(i)


def one_game(mat, change_n, change_m):
    global temp_answer
    global answer
    temp_answer = 0
    for i in range(n):
        for j in range(m):
            if mat[change_n][j] != 2:
                continue
            else:
                x = change_n # 현재 공격하는 궁수의 좌표
                y = j # 현재 공격하는 궁수의 좌표
                w_breaker = False
                for w in range(change_n - 1, -1, -1):
                    for q in range(change_m):
                        if mat[w][q] == 0:
                            continue
                        else:
                            distance = abs(w - x) + abs(q - y)
                            if distance <= d:
                                mat[w][q] = 0
                                temp_answer += 1
                                w_breaker = True
                                break
                            else:
                                continue
                    if w_breaker == True:
                        w_breaker = False
                        break
        mat[change_n - 1] = mat[change_n]
        change_n -= 1
    if answer <= temp_answer:
        answer = temp_answer


for i in list(combinations(arr, 3)): #궁수가 배치 되는 경우만큰 실행하기
    temp_matrix = [0] * m # 성
    matrix.append(copy.deepcopy(temp_matrix))

    for x in i:
        matrix[n][x] = 2
    one_game(copy.deepcopy(matrix) ,n , m)
    matrix.pop()


print(answer)
