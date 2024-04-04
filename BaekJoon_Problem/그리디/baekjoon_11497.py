import sys

test_case = int(sys.stdin.readline())

answer = []
for _ in range(test_case):
    N = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split(" ")))
    l.sort()
    result = 0
    for i in range(2, N):
        result = max(result, abs(l[i] - l[i - 2]))
    answer.append(result)

for a in answer:
    print(a)