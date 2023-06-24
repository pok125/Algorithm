n, m = map(int, input().split(" "))
board = [[0] * n for _ in range(n)]
visited = [0] * n

l = [list(map(int, input().split(" "))) for _ in range(m)]

for s, e in l:
    board[s - 1][e - 1] = 1
    board[e - 1][s - 1] = 1

for i in board:
    print(i)