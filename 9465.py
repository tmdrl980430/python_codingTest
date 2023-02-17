import sys

T = int(sys.stdin.readline())
            
for _ in range(T):
    n = int(sys.stdin.readline())
    
    arr =[list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    cache = [[0] * n for _ in range(2)]
    cache[0][0] = arr[0][0]
    cache[1][0] = arr[1][0]
    cache[0][1] = arr[0][1] + cache[1][0]
    cache[1][1] = arr[1][1] + cache[0][0]

    for i in range(2 , n):
        cache[0][i] = max(cache[1][i-2],cache[1][i-1]) + arr[0][i]
        cache[1][i] = max(cache[0][i-2],cache[0][i-1]) + arr[1][i]
    
    print(max(cache[0][n-1],cache[1][n-1]))