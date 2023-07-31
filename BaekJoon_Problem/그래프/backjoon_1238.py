import heapq

def dijkstra(start):
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if distance[cur_node] < cur_distance:
            continue

        for next_distance, next_node in graph[cur_node]:
            total_distance = cur_distance + next_distance

            if total_distance < distance[next_node]:
                distance[next_node] = total_distance
                heapq.heappush(queue, (total_distance, next_node))

N, M, X = map(int, input().split(" "))

graph = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)

for _ in range(M):
    s, e, w = map(int, input().split(" "))
    graph[s].append((w, e))

for i in range(1, N + 1):
    distance = [float('INF')] * (N + 1)
    dijkstra(i)
    
    if i == X:
        for j in range(1, N + 1):
            ans[j] += distance[j]
    else:
        ans[i] += distance[X]

print(max(ans))