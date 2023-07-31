N, M = map(int, input().split(" "))
graph = [[float("INF")] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    s, e = map(int, input().split(" "))
    graph[s - 1][e - 1] = 1
    graph[e - 1][s - 1] = 1

# 거쳐갈 노드 수
for k in range(N):
    # 시작
    for i in range(N):
        # 끝
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_sum = float('INF')
index = 0
for i in range(N):
    v = sum(graph[i])
    if min_sum > v:
        min_sum = v
        index = i

print(index + 1)