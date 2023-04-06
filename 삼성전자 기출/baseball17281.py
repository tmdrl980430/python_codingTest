import sys
from collections import deque

n = int(input())

game_score = []
for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    game_score.append(temp_arr)

out_cnt = 0
        
score = 0
score_list = []

def game(first):
    global score , out_cnt, game_score, score_list
    best_player_count = 0
    best_player_cnt = 0
    play_list = []
    base = deque()
    for i in range(3):
        base.append(0)
    first_player = first
    temp_player = -1
    ening = 0
    while ening < n:
        best_player_count += 1
        best_player_cnt += 1
        if best_player_count == 4:
            temp_player = first_player
            first_player = 0
        elif best_player_count == 5:
            first_player = temp_player
        elif best_player_cnt == 9:
            best_player_cnt = 0
            best_player_count = 0
        play_list.append(first_player)
        if game_score[ening][first_player] == 0:
            out_cnt += 1
            if out_cnt == 3:
                out_cnt = 0
                ening += 1
                first_player += 1
                if first_player == 9:
                    first_player = 1
                continue
        elif game_score[ening][first_player] == 1 or game_score[ening][first_player] == 2 or game_score[ening][first_player] == 3 or game_score[ening][first_player] == 4:
            for i in range(game_score[ening][first_player]):
                temp = base.pop()
                if temp == 1:
                    score += 1
                if i == 0:
                    base.appendleft(1)
                else:
                    base.appendleft(0)
        first_player += 1
        if first_player == 9:
            first_player = 1
    score_list.append(score)
    print(play_list)
    print("scores", score)

for i in range(1, 9):
    out_cnt = 0
    score = 0
    game(i)
print(score_list)
print(max(score_list))
