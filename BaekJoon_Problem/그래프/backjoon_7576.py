def bfs(tomato_pos):
    global count
    queue = []
    queue.append(tomato_pos)

    pos= [0, 0]
    while queue:
        pos_list = queue.pop(0)
        count += 1
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
                visited[pos[0]][pos[1]] = count
                
        if temp_list:
            queue.append(temp_list)
    

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

bfs(tomato)      
answer = count  
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and visited[i][j] == 0:
            answer = -1
            break
answer = answer - 1 if answer is not -1 else -1
print(answer)
