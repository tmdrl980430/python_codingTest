import sys

N = int(input())
cache = [-1] * (N + 1)
cache[0] = 0
cache[1] = 1

def fibo(n):
    if cache[n] != -1:
        return cache[n]
    
    cache[n] = fibo(n-2) + fibo(n-1)
    return cache[n]

result = fibo(N)
print(result)