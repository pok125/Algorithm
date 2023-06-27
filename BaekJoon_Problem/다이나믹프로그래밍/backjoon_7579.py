n, m = map(int, input().split(" "))
memorys = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))

board = [[0] * m for _ in range(n)]

pre_temp = 0
for i in range(1, n):
    for j in range(1, m):
        if j - memorys[i] < 0:
            pre_temp = 0
        else:
            pre_temp = board[i - 1][j - memorys[i]] + c[i]