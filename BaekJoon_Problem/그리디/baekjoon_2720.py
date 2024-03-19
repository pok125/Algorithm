import sys

N = int(sys.stdin.readline())
moneys = [int(sys.stdin.readline()) for _ in range(N)]

rest = [25, 10, 5, 1]
answer = []
for money in moneys:
    for r in rest:
        answer.append(money // r)
        money = money % r

for i in range(0, len(answer), 4):
    print(f"{answer[i]} {answer[i + 1]} {answer[i + 2]} {answer[i + 3]}")
