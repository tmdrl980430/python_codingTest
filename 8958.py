import sys

n = int(input())
sum = 0
for i in range(n):
    sum = 0
    a = input()
    score = 0
    for j in a:
        if j == 'O':
            if score != 0:
                score += 1
            else:
                score = 1
        else:
            score = 0
        sum += score 
    print(sum)           