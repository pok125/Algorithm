import sys

def dfs():
    root = 1
    stack = []
    parants[1] = 1
    stack.append(root)

    while stack:
        node = stack.pop()
        nodes = graph[node]

        for n in nodes:
            if parants[n] != 0:
                continue

            parants[n] = node
            stack.append(n)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
parants = [0 for _ in range((N + 1))]
for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split(" "))
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs()

for i in range(2, N + 1):
    print(parants[i])