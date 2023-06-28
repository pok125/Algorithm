n = int(input())
data = [list(map(int, input().split(' '))) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, len(data[i - 1]) + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + data[i - 1][j - 1]

print(max(dp[n])) 