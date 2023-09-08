import sys

n = int(sys.stdin.readline())

tree = {}

for i in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split())
    
    if a in tree:
        tree[a].append([b,c])
    else:
        tree[a] = [[b,c]]
        
    if b in tree:
        tree[b].append([a,c])
    else:
        tree[b] = [[a,c]]
distance = [0 for _ in range(n)]

print(tree)