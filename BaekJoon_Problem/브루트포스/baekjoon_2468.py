def bfs(pos, height):
    queue = []
    queue.append(pos)

    posX, posY = 0, 0
    while queue:
        x, y = queue.pop(0)

        for check_x, check_y in check_pos:
            posX = x + check_x
            posY = y + check_y

            if posX >= n or posX < 0 or posY >= n or posY < 0:
                continue
            if visited[posY][posX]:
                continue
            if height_list[posY][posX] <= height:
                continue

            visited[posY][posX] = True
            queue.append((posX, posY))

def solving(height):
    count = 0

    for i in range(n):
        for j in range(n):
            if not(visited[i][j]) and height_list[i][j]  > height:
                bfs((j, i), height)
                count += 1
    
    return count

def clear_board(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j] = False
                
n = int(input())
height_list = [list(map(int, input().split(" "))) for _ in range(n)]

check_pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * n for _ in range(n)]
answer = 0

for h in range(100):
    answer = max(answer, solving(h))
    clear_board(visited)

print(answer)