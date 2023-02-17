import sys

n = int(sys.stdin.readline())
cache = [0] * (n+1)

def f(n):
    if n <= 2:
        return n
    elif cache[n] != 0:
        return cache[n]
    
    for i in range(3, n+1):
        cache[i] = (f(i -1) + f(i - 2))
        
    return cache[n]

print(f(n) % 10007)