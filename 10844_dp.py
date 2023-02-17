import sys
MOD = 1000000000
n = int(sys.stdin.readline())

cache = [[0] * 10 for _ in  range(n+1)]

def f(n, d):
    if n == 1:
        if d == 0:
            return 0
        else:
            return 1
    if cache[n][d] != 0:
        return cache[n][d]
    if d > 0:
        cache[n][d] += f(n-1,d-1)
        cache[n][d] %= MOD
    if d <9:
        cache[n][d] += f(n-1,d+1)
        cache[n][d] %= MOD

        
    return cache[n][d]

    
print(sum(f(n, i) for i in range(10)) % MOD)