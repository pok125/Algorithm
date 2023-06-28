def dp(N):
    dp_data = [1] * 3

    for i in range(3, N):
        dp_data.append(dp_data[i - 2] + dp_data[i - 3])
    
    return dp_data[N - 1]

case_count = int(input())
answer = []
for _ in range(case_count):
    n = int(input())
    answer.append(dp(n))

for i in answer:
    print(i)