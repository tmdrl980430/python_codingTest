import sys

h,m,s = map(int, sys.stdin.readline().split())

add = int(sys.stdin.readline())

s += add

while s >= 60:
    s -= 60
    m += 1

while m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24
    
print(h, end=' ')
print(m, end=' ')
print(s)