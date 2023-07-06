n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

dp[1] = l[0]

if n == 1:
    print(dp[1])
else:
    dp[2] = dp[1] + l[1]

    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + l[i - 2] + l[i - 1]
        dp[i] = max(dp[i], dp[i - 2] + l[i - 1])
        dp[i] = max(dp[i], dp[i - 1])
    
    print(dp[n])