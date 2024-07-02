import sys
import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        distance, current = heapq.heappop(pq)
        if d[current] < distance: continue
        for n, w in graph[current]:
            next_distance = distance + w
            if next_distance < d[n]:
                d[n] = next_distance
                heapq.heappush(pq, (next_distance, n))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e, w = map(int, sys.stdin.readline().split(" "))
    graph[s].append((e, w))

start_num, end_num = map(int, sys.stdin.readline().split(" "))
d = [float("INF") for _ in range(N + 1)]

dijkstra(start_num)
print(d[end_num])