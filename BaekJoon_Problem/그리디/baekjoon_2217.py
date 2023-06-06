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