import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))
l.sort()
print(l[(N - 1) // 2])