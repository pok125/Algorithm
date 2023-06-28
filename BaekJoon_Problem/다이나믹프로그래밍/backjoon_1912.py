n = int(input())
l = list(map(int, input().split(" ")))
dp = [0] * (n + 1)

hap = 0
for i in range(1, n + 1):
    hap = dp[i - 1] + l[i - 1]
    dp[i] = hap if hap > 0 else 0

answer = max(dp[1:])
if answer <= 0:
    answer = max(l)
print(answer)