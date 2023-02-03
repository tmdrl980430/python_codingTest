import sys

n,k = map(int, sys.stdin.readline().split())

coin_arr = []
for i in range(n):
    coin = int(input())
    coin_arr.append(coin)

coin_arr.sort(reverse=True)

answer = 0
for i in coin_arr:
    if k // i > 0:
        answer += k // i
        k -= (k//i) * i
print(answer)