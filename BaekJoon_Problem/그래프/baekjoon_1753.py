import sys
import heapq

def diijkstra(start_node):
    d[start_node] = 0
    
    pq = []
    pq.append((0, start_node))
    heapq.heapify(pq)
    while pq:
        cur_distance, cur_node = heapq.heappop(pq)

        if d[cur_node] < cur_distance:
            continue

        for next_distance, next_node in graph[cur_node]:
            total_distance = cur_distance + next_distance
            if total_distance < d[next_node]:
                d[next_node] = total_distance
                heapq.heappush(pq, (total_distance, next_node))

    
V, E = map(int, input().split(" "))
start = int(input()) - 1
graph = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split(" "))
    graph[s - 1].append((w, e - 1))

d = [float("INF")] * V

diijkstra(start)

for i in d:
    if i == float("INF"):
        print("INF")
    else:
        print(i)