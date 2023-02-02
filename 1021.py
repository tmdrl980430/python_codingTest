from collections import deque
import sys

n , m = map(int, sys.stdin.readline().split())

temp_queue1 = deque()
temp_queue2 = deque()



for i in range(1, n+1):
    temp_queue1.append(i)
    temp_queue2.append(i)
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(len(arr)):
    answer1 = 0
    answer2 = 0
    length = len(temp_queue1)
    for z in range(2):
        for j in  range(length):
            if z == 0:
                temp = temp_queue1.popleft()
            else:
                temp = temp_queue2[0]
            if temp == arr[i]:
                if z == 1:
                    temp_queue2.popleft()
                break
            else:
                if z == 0:
                    answer1 += 1
                    temp_queue1.append(temp)
                else:
                    answer2 += 1
                    temp = temp_queue2.pop()
                    temp_queue2.appendleft(temp)
                continue
            
        
    if  answer1 == answer2:
        answer += answer1
    elif answer1 < answer2:
        answer += answer1
    else:
        answer += answer2
        


print(answer)
