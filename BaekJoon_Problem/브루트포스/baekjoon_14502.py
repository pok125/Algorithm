import sys

n, m = map(int, input().split(" "))
board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]

check_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
virus_pos = []
safe_pos = []
answer = []

for row in range(n):
    for col in range(m):
        if board[row][col] == 2:
            virus_pos.append((col, row))
        elif board[row][col] == 0:
            safe_pos.append((col, row))

def solving(bolck_count, board):
    if bolck_count == 3:
        safe_count = bfs(board)
        answer.append(safe_count)
        return

    for x, y in safe_pos:
        if board[y][x] == 0:    
            board[y][x] = 1
            solving(bolck_count + 1, board)
            board[y][x] = 0

def bfs(board):
    visited = [[False] * m for _ in range(n)]
    queue = virus_pos.copy()

    x, y = 0, 0
    posx, posy = 0, 0
    while queue:
        x, y = queue.pop(0)
        visited[y][x] = True

        for checkx, checky in check_pos:
            posx = x + checkx
            posy = y + checky

            if posx >= m or posx < 0 or posy >= n or posy < 0:
                continue
            if visited[posy][posx]:
                continue

            if board[posy][posx] == 0:
                queue.append((posx, posy))
                visited[posy][posx] = True

    count = 0
    for i in range(n):
        for j in range(m):
            if not(visited[i][j]) and board[i][j] == 0:
                count += 1

    return count

solving(0, board)
print(max(answer))