test_case = int(input())
answer = []

for _ in range(test_case):
    n = int(input())
    dp = [[0] * 2 for _ in range(n + 1)]
    
    dp[0][0] = 1
    dp[0][1] = 0
    
    if n >= 1:
        dp[1][0] = 0
        dp[1][1] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    
    answer.append(dp[n])

for zero, one in answer:
    print(f'{zero} {one}')