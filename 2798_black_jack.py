from itertools import combinations

n, m = map(int, input().split())

cards = list(map(int, input().split()))

max = 0 


arr = combinations(cards, 3)

for i in arr:
    temp = sum(i)
    if temp == max:
        continue
    if temp > m:
        continue
    if temp == m :
        max = temp
        break
    
    if temp < m:
        if max <= temp:
            max = temp
        else:
            continue
    
print(max)