import sys

N = int(sys.stdin.readline())

answer = 0
while N > 0:
    if N % 5 == 0:
        answer += N // 5
        N = 0
        break

    N -= 2
    answer += 1

answer = answer if N == 0 else -1
print(answer)
