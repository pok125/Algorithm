import sys

def bfs(pos):
    global count
    if visited[pos[0]][pos[1]]:
        return
    
    queue = []
    queue.append(pos)
    visited[pos[0]][pos[1]] = 1
    count += 1

    temp_pos = [0, 0]
    while queue:
        cur_pos = queue.pop(0)

        for check in check_pos:
            temp_pos[0] = cur_pos[0] + check[0]
            temp_pos[1] = cur_pos[1] + check[1]

            if temp_pos[0] >= h or temp_pos[0] < 0 or temp_pos[1] >= w or temp_pos[1] < 0:
                continue
            if visited[temp_pos[0]][temp_pos[1]]:
                continue
            if board[temp_pos[0]][temp_pos[1]] == 0:
                continue

            queue.append(temp_pos.copy())
            visited[temp_pos[0]][temp_pos[1]] = 1
    

answer = []
check_pos = [
    (1, 0), 
    (-1, 0), 
    (0, -1), 
    (0, 1), 
    (1, -1), 
    (1, 1),
    (-1, -1),
    (-1, 1)
    ]
count = 0
while True:
    w, h = map(int, input().split(" "))
    if w == 0 and h == 0:
        break

    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                continue
            bfs((i, j))
    
    answer.append(count)

for i in answer:
    print(i)