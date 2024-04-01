import sys

N, M = map(int, sys.stdin.readline().split(" "))
J = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(J)]

s, e = 1, M
hap = 0
for apple in l:
    if apple > e:
        hap += apple - e
        e = apple
        s = e - M + 1
    elif apple <= e and s > apple:
        hap += s - apple
        s = apple
        e = s + M - 1
print(hap)