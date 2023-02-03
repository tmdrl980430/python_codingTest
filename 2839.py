from collections import deque

answer = 0

n = int(input())

temp = n // 5


while temp >= 0:
    sum = n - temp * 5
    if sum % 3 == 0:
        print(sum // 3 + temp)
        break
    if temp == 0 :
        print(-1)
    temp -= 1