def bfs(pos):
    global total_zone_count

    if visited[pos[0]][pos[1]]:
        return

    total_zone_count += 1
    queue = []
    queue.append(pos)
    visited[pos[0]][pos[1]] = 1

    temp_pos = [0, 0]
    count = 1
    while queue:
        cur_pos = queue.pop(0)
        
        for i in check_pos:
            temp_pos[0] = cur_pos[0] + i[0]
            temp_pos[1] = cur_pos[1] + i[1]

            if temp_pos[0] >= n or temp_pos[0] < 0 or temp_pos[1] >= n or temp_pos[1] < 0:
                continue
            if board[temp_pos[0]][temp_pos[1]] == "0":
                continue
            if visited[temp_pos[0]][temp_pos[1]]:
                continue
            
            queue.append((temp_pos[0], temp_pos[1]))
            visited[temp_pos[0]][temp_pos[1]] = 1
            count += 1
    
    answer.append(count)
  
check_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(input())
board = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
total_zone_count = 0
zone_pos = []
answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == "1":
            zone_pos.append((i, j))

for pos in zone_pos:
    bfs(pos)

print(total_zone_count)
answer.sort()
for ans in answer:
    print(ans)