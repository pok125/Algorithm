def bfs(pos, isnormal= True):
    global count1, count2
    if visited[pos[0]][pos[1]]:
        return
    
    queue = []
    queue.append(pos)
    visited[pos[0]][pos[1]] = 1
    temp_pos = [0] * 2
    color = board[pos[0]][pos[1]]

    while queue:
        cur_pos = queue.pop(0)

        for check in check_pos:
            temp_pos[0] = cur_pos[0] + check[0]
            temp_pos[1] = cur_pos[1] + check[1]

            if temp_pos[0] >= n or temp_pos[1] >= n or temp_pos[0] < 0 or temp_pos[1] < 0:
                continue
            if visited[temp_pos[0]][temp_pos[1]]:
                continue
            if board[temp_pos[0]][temp_pos[1]] is not color:
                continue
            
            queue.append(temp_pos.copy())
            visited[temp_pos[0]][temp_pos[1]] = 1

    if isnormal:
        count1 += 1
    else:
        count2 += 1


n = int(input())
board = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
check_pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count1, count2 = 0, 0

for i in range(n):
    for j in range(n):
        bfs((i, j))

visited = [[0] * n for _ in range(n)]
for i in range(n):
    board[i] = board[i].replace("G", "R")
    
for i in range(n):
    for j in range(n):
        bfs((i, j), False)

print(f"{count1} {count2}")