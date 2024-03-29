import sys
from collections import deque
from itertools import permutations

n = int(input())

game_score = []
sort_list = []
for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    game_score.append(temp_arr)

for i in range(9):
    sort_list.append(i)
sort_list = list(permutations(sort_list, 9))

out_cnt = 0
        
score = 0
score_list = [0]

def game(order):
    global score , out_cnt, game_score, score_list
    best_player_cnt = 0
    base = deque()
    for i in range(3):
        base.append(0)
    ening = 0
    while ening < n:

        if game_score[ening][order[best_player_cnt]] == 0:
            out_cnt += 1
            if out_cnt == 3:
                out_cnt = 0
                ening += 1
                base = deque()
                for i in range(3):
                    base.append(0)
                best_player_cnt += 1
                if best_player_cnt == 9:
                    best_player_cnt = 0
                continue
        elif game_score[ening][order[best_player_cnt]] == 1 or game_score[ening][order[best_player_cnt]] == 2 or game_score[ening][order[best_player_cnt]] == 3 or game_score[ening][order[best_player_cnt]] == 4:
            for i in range(game_score[ening][order[best_player_cnt]]):
                temp = base.pop()
                if temp == 1:
                    score += 1
                if i == 0:
                    base.appendleft(1)
                else:
                    base.appendleft(0)

        best_player_cnt += 1
        if best_player_cnt == 9:
            best_player_cnt = 0
    if max(score_list) < score:
        score_list.append(score)



for i in sort_list:
    out_cnt = 0
    score = 0
    if i[3] == 0:
        game(i)
print(max(score_list))
