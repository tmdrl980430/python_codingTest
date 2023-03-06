import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

count_arr = []
MAX = 10 ** 5
dist = [0] * (MAX+1)
def bfs():
    queue = deque()
    queue.append(n)
    count = 1
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for i in range(3):
            if i == 0:
                nx =  x + 1
            elif i == 1:
                nx =  x - 1
            else:
                nx = x * 2
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
bfs()