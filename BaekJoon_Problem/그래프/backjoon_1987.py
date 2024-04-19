import sys

# 재귀
def dfs(x, y, cnt):
    global count
    count = max(count, cnt)

    for dirX, dirY in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        posX, posY = x + dirX, y + dirY

        if posX < 0 or posX >= R or posY < 0 or posY >= C:
            continue
        if visited[ord(board[posX][posY]) - ord("A")] != 0:
            continue
        
        visited[ord(board[posX][posY]) - ord("A")] = 1
        dfs(posX, posY, cnt + 1)
        visited[ord(board[posX][posY]) - ord("A")] = 0

R, C = map(int, sys.stdin.readline().split(" "))
board = [sys.stdin.readline().rstrip() for _ in range(R)]
visited = [0] * (ord("Z") - ord("A") + 1) 
count = 1
visited[ord(board[0][0]) - ord("A")] = 1
dfs(0, 0, count)
print(count)