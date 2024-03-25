from collections import Counter

n = int(input())
l = [int(input()) for _ in range(n)]
d = Counter(l)
keys = sorted(d)

result = 0
w = 0
count = 0
for i in range(len(keys)):
    w = keys[i] * (n - count)
    if result < w:
        result = w
    count += d[keys[i]]

print(result)

# 다른 풀이
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort(reverse=True)
answer = 0

for i, num in enumerate(nums, start=1):
    answer = max(answer, num * i)

print(answer)