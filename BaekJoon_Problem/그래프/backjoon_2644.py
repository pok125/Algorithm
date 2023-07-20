def bfs():
    queue = []
    queue.append(start)
    visited[start] = 1

    while queue:
        cur_node = queue.pop(0)

        if cur_node == end:
            return visited[end] - 1

        for node in graph[cur_node]:
            if visited[node]:
                continue
            
            queue.append(node)
            visited[node] += visited[cur_node] + 1
    
    return -1


n = int(input())
start, end = map(int, input().split(" "))
start -= 1
end -= 1
m = int(input())
graph = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    s, e = map(int, input().split(" "))
    graph[s - 1].append(e - 1)
    graph[e - 1].append(s - 1)

print(bfs())