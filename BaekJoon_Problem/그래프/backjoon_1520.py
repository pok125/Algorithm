def dfs(ci, cj):
    if dp[ci][cj] == -1:
        dp[ci][cj] = 0
        
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            pi, pj = ci + di, cj + dj
            
            if pi >= N or pi < 0 or pj >= M or pj < 0:
                continue
            if board[pi][pj] > board[ci][cj]:
                dp[ci][cj] += dfs(pi, pj)

    return dp[ci][cj]

N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[0][0] = 1
print(dfs(N - 1, M - 1))