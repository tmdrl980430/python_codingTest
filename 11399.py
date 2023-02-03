import sys

n = input()

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
sum = 0
for i in range(len(arr)):

    for j in range(0,i+1):
        sum += arr[j]
print(sum)