N, M = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for a, b in info:
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for curr in graph[v]:
        if not visited[curr]:
            visited[curr] = True
            dfs(curr)

visited[1] = True
dfs(1)

print(sum(visited)-1)


