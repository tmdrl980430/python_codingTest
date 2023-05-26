import sys
from collections import deque
from itertools import combinations


n, k = map(int, input().split())

bags = []


for i in range(n):
    #입력
    w, v = map(int, input().split())
    bags.append((w,v))

bags2 = []

max_count = 0
for j in range(1,n+1):
    bags2= combinations(bags,j)

    for i in bags2:
        sum = 0
        #가지고 있는 거의 무게
        have_weights = 0
        have_value = 0
        for z in range(len(i)):
            have_weights += i[z][0]
            have_value += i[z][1]
            if have_weights > k:
                sum = 0
                break
            
        if have_weights <= k:
            sum = have_value
        else:
            sum = 0
        
        if sum >= max_count:
            max_count = sum

print(max_count)

