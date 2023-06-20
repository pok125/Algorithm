f = [[0] * 15 for _ in range(15)]

for floor in range(15):
    for num in range(1, 15):
        if floor == 0:
            f[floor][num] = num
        else:
            f[floor][num] = f[floor][num - 1] + f[floor - 1][num]

test_case = int(input())
answer = []
for i in range(test_case):
    k = int(input())
    n = int(input())

    answer.append(f[k][n])

for i in answer:
    print(i)