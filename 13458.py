import sys

n = int(sys.stdin.readline())

test_room = list(map(int, sys.stdin.readline().split()))

b,c = map(int, sys.stdin.readline().split())
count = 0
for i in test_room:
    temp = i
    count += 1
    temp -= b
    if temp > 0:
        count += (temp // c)
        if temp % c != 0:
            count += 1

print(count)