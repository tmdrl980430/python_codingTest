import sys
from collections import deque

#수빈이는 걷는다면 좌우 이동(x-1 or x+1) 1초 걸림
#수빈이는 순간이동 0초 후에 2*X의 위치로 이동


n ,k = map(int, sys.stdin.readline().split())

MAX = 100000

visited =[False] * (MAX + 1)
distance = [0] * (MAX + 1)

visited[n] = True
distance[n] = 0

queue = deque()
queue.append(n)

while queue:
    node = queue.popleft()
    if node * 2 < MAX and visited[node * 2] == False:
        distance[node * 2] = distance[node]
        visited[node] = True
        queue.append(node*2)
    if node + 1< MAX and visited[node+1] == False :
        distance[node+1] = distance[node] + 1
        visited[node+1] = True
        queue.append(node+1)
    if node - 1 < MAX and node - 1 >= 0 and visited[node-1] == False:
        distance[node-1] = distance[node] + 1
        visited[node-1] = True
        queue.append(node-1)

print(distance)