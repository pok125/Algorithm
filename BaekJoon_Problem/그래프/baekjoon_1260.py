def bfs(start_node):
    queue = []
    queue.append(start_node)
    ans_bfs.append(start_node)

    visited[start_node] = 1

    while queue:
        cur_node = queue.pop(0)
        
        for node in graph[cur_node]:
            if not visited[node]:
                visited[node] = 1
                ans_bfs.append(node)
                queue.append(node)
                
            
def dfs(start_node):
    visited[start_node] = 1
    ans_dfs.append(start_node)

    for node in graph[start_node]:
        if not visited[node]:
            dfs(node)
                
                
n, m, s = map(int, input().split(" "))
l = [list(map(int, input().split(" "))) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans_dfs = []
ans_bfs = []

for start, next in l:
    graph[start].append(next)
    graph[next].append(start)

for i in range(1, len(graph)):
    graph[i].sort()

dfs(s)
for i in range(len(visited)):
    visited[i] = 0
bfs(s)
print(*ans_dfs)
print(*ans_bfs)