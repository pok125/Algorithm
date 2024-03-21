import sys
R, C = map(int, sys.stdin.readline().split(" "))
board = [sys.stdin.readline() for _ in range(R)]
visited = [[0] * C for _ in range(R)]

answer = 0
def dfs(start):
    stack = []
    stack.append(start)

    result = 0
    while stack:
        X, Y = stack.pop()
        visited[X][Y] = 1

        if Y == (C - 1):
            result = 1
            return result

        for posX, posY in [(1, 1), (0, 1), (-1, 1)]:
            checkX = X + posX
            checkY = Y + posY

            if checkX < 0 or checkY < 0 or checkX >= R or checkY >= C:
                continue
            if board[checkX][checkY] == "x":
                continue
            if visited[checkX][checkY] == 1:
                continue

            stack.append((checkX, checkY))
            
    return result

for i in range(R):
    if board[i][0] == "x":
        continue
    
    answer += dfs((i, 0))

print(answer)