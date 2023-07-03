import sys

def bfs(tomato_list):
    global count
    queue = []
    queue.append(tomato_list)

    temp_pos = [0] * 2
    
    temp_list = []
    while queue:
        cur_list = queue.pop(0)
        count += 1

        for pos in cur_list:
            check_list = []
            
            if pos[0] % N == 0:
                check_list = check_pos_top
            elif pos[0] % N == N - 1:
                check_list = check_pos_bottom
            else:
                check_list = check_pos_normal
            
            for check in check_list:
                temp_pos[0] = pos[0] + check[0]
                temp_pos[1] = pos[1] + check[1]

                if temp_pos[0] >= height or temp_pos[0] < 0 or temp_pos[1] >= M or temp_pos[1] < 0:
                    continue
                if board[temp_pos[0]][temp_pos[1]] != 0:
                    continue
                if visited[temp_pos[0]][temp_pos[1]] != 0:
                    continue
                
                temp_list.append((temp_pos[0], temp_pos[1]))
                visited[temp_pos[0]][temp_pos[1]] = count
        
        if temp_list:
            queue.append(temp_list.copy())
            temp_list.clear()

M, N, H = map(int, input().split(" "))
height = N * H
board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(height)]
visited = [[0] * M for _ in range(height)]
check_pos_normal = [(-1, 0), (1, 0), (0, 1), (0, -1), (N, 0), (-N, 0)]
check_pos_top = [(1, 0), (0, 1), (0, -1), (N, 0), (-N, 0)]
check_pos_bottom = [(-1, 0), (0, 1), (0, -1), (N, 0), (-N, 0)]

tomato = []
for i in range(height):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i, j))

count = 0
bfs(tomato)      
answer = count
flag = False 
for i in range(height):
    if flag:
        break

    for j in range(M):
        if board[i][j] == 0 and visited[i][j] == 0:
            answer = -1
            flag = True
            break
answer = answer - 1 if answer != -1 else -1
print(answer)