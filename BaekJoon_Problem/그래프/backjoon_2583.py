def bfs(pos):
    global total_count
    if visited[pos[0]][pos[1]]:
        return
    
    total_count += 1
    queue = []
    queue.append(pos)
    visited[pos[0]][pos[1]] = 1

    temp_pos = [0, 0]
    count = 1
    while queue:
        cur_pos = queue.pop(0)

        for check in check_pos:
            temp_pos[0] = cur_pos[0] + check[0]
            temp_pos[1] = cur_pos[1] + check[1]

            if temp_pos[0] >= M or temp_pos[0] < 0 or temp_pos[1] >= N or temp_pos[1] < 0: 
                continue
            if board[temp_pos[0]][temp_pos[1]]:
                continue
            if visited[temp_pos[0]][temp_pos[1]]:
                continue

            queue.append((temp_pos[0], temp_pos[1]))
            visited[temp_pos[0]][temp_pos[1]] = 1
            count += 1
    
    answer.append(count)


M, N, K = map(int, input().split(" "))
l = [list(map(int, input().split(" "))) for _ in range(K)]
board = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
check_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = []
total_count = 0
for x, y, endx, endy in l:
    for i in range(x, endx):
        for j in range(y, endy):
            board[j][i] = 1

for y in range(M):
    for x in range(N):
        if board[y][x]:
            continue
        bfs((y, x))

answer.sort()
print(total_count)
print(*answer)