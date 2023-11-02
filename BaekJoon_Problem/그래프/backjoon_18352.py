def bfs(graph, visited, start):
    global answer

    queue = []
    visited[start] = 1
    queue.append(start)
    
    while queue:
        cur_node = queue.pop(0)
        if visited[cur_node] > K:
            break

        for node in graph[cur_node]:
            if not node:
                continue
            if visited[node] != 0:
                continue
            if visited[cur_node] == K:
                answer.append(node + 1)

            queue.append(node)
            visited[node] = visited[cur_node] + 1

N, M, K, X = map(int, input().split(" "))
graph = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    s, e = map(int, input().split(" "))
    graph[s-1].append(e-1)

answer = []
bfs(graph, visited, X - 1)

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)