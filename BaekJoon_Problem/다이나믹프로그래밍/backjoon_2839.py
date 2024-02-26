# N킬로그램의 설탈 배달
# 3, 5킬로그램의 봉지가 있다.
# 적은 수의 봉지로 배달하려 한다.

N = int(input())
dp = [float("inf")] * (N + 1)
dp[3] = 1
if N >= 5:
    dp[5] = 1
for i in range(3, N + 1):
    if i - 3 >= 0:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i - 5] + 1)
answer = dp[N] if dp[N] != float("inf") else -1
print(answer)