def bfs(tomato_pos):
    global count
    queue = []
    queue.append(tomato_pos)

    pos= [0, 0]
    max_value = 0
    while queue:
        pos_list = queue.pop(0)

        temp_list = []        
        for i in pos_list:
            for check in check_pos:
                pos[0] = i[0] + check[0]
                pos[1] = i[1] + check[1]

                if pos[0] >= N or pos[0] < 0 or pos[1] >= M or pos[1] < 0:
                    continue
                if visited[pos[0]][pos[1]] != 0:
                    continue
                if board[pos[0]][pos[1]] != 0:
                    continue

                temp_list.append((pos[0], pos[1]))
                visited[pos[0]][pos[1]] = visited[i[0]][i[1]] + 1
                max_value = max(max_value, visited[pos[0]][pos[1]])
                count -= 1

        if temp_list:
            queue.append(temp_list)
    
    return max_value

check_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
M, N = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
tomato = []
count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i, j))
        elif board[i][j] == 0:
            count += 1

answer = bfs(tomato)
answer = answer if count == 0 else -1
print(answer)
