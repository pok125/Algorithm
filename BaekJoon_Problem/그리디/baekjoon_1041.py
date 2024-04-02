import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().strip().split(" ")))
answer = 0

if N == 1:
    l.sort()
    answer = sum(l) - l[-1]
else:
    min_lists = [min(l[i], l[5 - i]) for i in range(3)]
    min_lists.sort()

    min1 = min_lists[0]
    min2 = min_lists[0] + min_lists[1]
    min3 = sum(min_lists)

    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    answer += min1 * n1
    answer += min2 * n2
    answer += min3 * n3

print(answer)