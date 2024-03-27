import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

l.sort()

hap = 0
for i in range(N):
    if hap + 1 < l[i]:
        break
    hap += l[i]
print(hap + 1)
