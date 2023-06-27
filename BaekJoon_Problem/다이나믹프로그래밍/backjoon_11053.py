n = int(input())
l = [0] + list(map(int, input().split(" ")))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    cur_value = l[i]
    max_value = 0
    for j in range(i):
        if cur_value > l[j]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1
    
print(max(dp))