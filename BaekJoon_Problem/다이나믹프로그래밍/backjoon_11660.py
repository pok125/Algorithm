# x1, y1 ~ x2, y2까지 합 구하기
import sys

N, M = map(int, input().split(" "))
board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]    
pos_list = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i - 1][j - 1]

answer = []
for x1,y1,x2,y2 in pos_list:
    temp = dp[y2][x2]
    if x1 == x2 and y1 == y2:
        temp = board[y1 - 1][x1 - 1]
        answer.append(temp)
        continue
    if x1 == 1 and y1 == 1:
        answer.append(temp)
        continue
    temp -= dp[y2][x1 - 1]
    temp -= dp[y1 - 1][x2]
    temp += dp[y1 - 1][x1 - 1]
    
    answer.append(temp)

for i in answer:
    print(i)
    