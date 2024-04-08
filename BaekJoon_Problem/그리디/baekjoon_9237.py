import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

l.sort(reverse=True)

for i in range(N):
    l[i] += (i + 1)

print(max(l) + 1)