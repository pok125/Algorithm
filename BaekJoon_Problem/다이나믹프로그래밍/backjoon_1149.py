n = int(input())
l = [list(map(int, input().split(" "))) for _ in range(n)]

sum_list = [[0] * 3 for _ in range(n)]
sum_list[0] = l[0]

for i in range(1, n):
    sum_list[i][0] = min(sum_list[i - 1][1], sum_list[i - 1][2]) + l[i][0]
    sum_list[i][1] = min(sum_list[i - 1][0], sum_list[i - 1][2]) + l[i][1]
    sum_list[i][2] = min(sum_list[i - 1][0], sum_list[i - 1][1]) + l[i][2]

print(min(sum_list[n - 1]))