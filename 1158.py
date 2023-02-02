import sys

from collections import deque


# 전형적인 원형 큐 문제

n, k = map(int , sys.stdin.readline().split())


answer_arr = []
queue = deque()
for i in range(n):
    queue.append(i+1)

while queue:
    for i in range(k):
        temp = queue.popleft()
        if i < k-1:
            queue.append(temp)
        else:
            answer_arr.append(temp)

print("<", end="")
for i in range(n):
    if i != n-1:
        print(answer_arr[i], end=", ")
    else:
        print(answer_arr[i], end=">")