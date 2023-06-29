import sys

def bfs(start_node):
    global answer

    if visited[start_node] == 1:
        return
    
    queue = []
    queue.append(start_node)
    visited[start_node] = 1
    answer += 1

    while queue:
        cur_node = queue.pop(0)

        for node in range(n):
            if board[cur_node][node] == 0:
                continue
            if visited[node] == 1:
                continue

            queue.append(node)
            visited[node] = 1

n, m = map(int, sys.stdin.readline().split(" "))
board = [[0] * n for _ in range(n)]
visited = [0] * n

l = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(m)]

for s, e in l:
    board[s - 1][e - 1] = 1
    board[e - 1][s - 1] = 1

answer = 0
for i in range(n):
    bfs(i)
print(answer)