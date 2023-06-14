def dfs():
    global count
    queue = []
    queue.append(1)
    visited[1] = 1

    while queue:
        cur_node = queue.pop(0)
        
        for node in graph[cur_node]:
            if visited[node]:
                continue

            visited[node] = 1
            count += 1
            queue.append(node)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    start, next = map(int, input().split(" "))
    graph[start].append(next)
    graph[next].append(start)

count = 0
dfs()
print(count)