import sys

N = int(input())
M = int(input())
infos = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

graph = [[float("INF")] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for s, e, w in infos:
    if graph[s - 1][e - 1] != float("INF"):
        graph[s - 1][e - 1] = min(graph[s - 1][e - 1], w)
    else:
        graph[s - 1][e - 1] = w

# 거쳐갈 노드 수
for k in range(N):
    # 시작
    for i in range(N):
        # 끝
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
    for j in i:
        if j == float("INF"):    
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()