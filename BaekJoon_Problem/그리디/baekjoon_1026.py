import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))
B = list(map(int, sys.stdin.readline().split(" ")))

A.sort()
B.sort(reverse=True)

print(sum(map(lambda x:x[0] * x[1], zip(A, B))))
