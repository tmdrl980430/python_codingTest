import sys
import heqpq


n = int(sys.stdin.readline())


numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))
    numbers.sort()
    if len(numbers) % 2 == 1:
        #홀수일 때
        print(numbers[len(numbers)//2])
    else:
        print(numbers[len(numbers)//2-1])