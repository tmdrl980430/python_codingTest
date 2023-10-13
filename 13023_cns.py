n , m = map(int, input().split())

answers = False
relation = [[] for _ in range(n)]

visited = [False] * 2001

for i in range(m):
    a ,b = map(int, input().split())

    relation[a].append(b)
    relation[b].append(a)


def dfs(idx, depth):
    global answers
    visited[idx] = True
    if depth == 4:
        answers = True
        return
    for i in relation[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answers:
        break
    
if answers:
    print(1)
else:
    print(0)
