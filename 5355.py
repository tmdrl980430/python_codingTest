import sys

n = int(sys.stdin.readline())

data = [sys.stdin.readline().strip() for i in range(n)]

for j in range(len(data)):
    arr =[]
    arr = data[j].split()
    a = float(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] == '@':
            a *= 3
        elif arr[i] == '%':
            a += 5
        elif arr[i] == '#':
            a -= 7
    print(format(a,".2f"))
    
    