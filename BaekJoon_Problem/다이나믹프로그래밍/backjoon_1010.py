test_case = int(input())
answer = []
facto = [0] * 31
facto[0] = 1
facto[1] = 1

for i in range(2, 31):
    facto[i] = facto[i - 1] * i

temp = 0
for _ in range(test_case):
    N, M = map(int, input().split(" "))
    temp = int(facto[M] / (facto[N] * facto[M - N]))
    answer.append(temp)

for i in answer:
    print(i)