import sys

from collections import deque

 #풍선 종이에 적혀 있는 숫자만큼 이동한다.
 #단, 이미 터진 풍선은 건너뛴다
 
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dict = {}
queue = deque()
for i in range(len(arr)):
    dict[arr[i]] = i + 1
    queue.append(arr[i])
i = 0
answer = []
while queue:
    tmp = 0
    if i == 0:
        temp = queue.popleft()
        answer.append(dict[temp])
        i +=1
        continue
    if temp > 0:
        for j in range(temp):
            tmp = queue.popleft()
            queue.append(tmp)
        temp = queue.pop()  
    else:
        temp *= -1
        for j in  range(temp):
            tmp = queue.pop()
            queue.appendleft(tmp) 
        temp = queue.popleft()             
    answer.append(dict[temp])
    i += 1

for i in range(len(answer)):
    if i == len(answer)-1:
        print(answer[i], end="")
    else:
        print(answer[i], end=" ")