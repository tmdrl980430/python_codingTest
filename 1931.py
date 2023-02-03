import sys

n = int(input())

arr = []
for i in range(n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    arr.append(temp_arr)

arr = sorted(arr,key=lambda x:x[1])
temp1 = 0
answer = 0
for i in range(n):
    
    if i == 0:
        temp1 = arr[i][1]
        answer += 1
        continue
    elif temp1 <= arr[i][0]:
        temp1 = arr[i][1]
        answer += 1
        
print(answer)
