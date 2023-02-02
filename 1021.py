from collections import deque
import sys

n , m = map(int, sys.stdin.readline().split())
arr_queue = deque()

for i in range(1, n+1):
    arr_queue.append(i)
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
# for i in range(len(arr)):
#     for j in  range(len(arr_queue)):
        
#         temp = arr_queue.popleft()
        
#         if temp == arr[i]:
#             break
#         else:
#             continue
rightMove()
print(arr_queue)
leftMove()
print(arr_queue)

def rightMove():
    tempRight = arr_queue.popleft()
    arr_queue = arr_queue.append(tempRight)

def leftMove ():
    tempLeft = arr_queue.pop()
    arr_queue = arr_queue.appendleft(tempLeft)
print(answer)
