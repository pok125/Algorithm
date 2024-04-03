import sys
N = int(sys.stdin.readline())
ranks = [int(sys.stdin.readline()) for _ in range(N)]
ranks.sort()
hap = 0

for i in range(1, N + 1):
    if ranks[i - 1] != i:
        hap += abs(i - ranks[i - 1])
print(hap)