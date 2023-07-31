N, K = map(int, input().split(" "))
l = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        # 선택 x
        v1 = dp[i - 1][j]
        # 무게가 충족 되면 선택
        v2 = 0
        if j - l[i - 1][0] >= 0:
            v2 = dp[i - 1][j - l[i - 1][0]] + l[i - 1][1]
        dp[i][j] = max(v1, v2)

print(dp[N][K])
