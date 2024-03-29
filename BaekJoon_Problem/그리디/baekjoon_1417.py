import sys

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in (range(N))]

dasom = l.pop(0)
l.sort(reverse=True)

count = 0
max_num = l[0] if l else 0
while l and dasom <= max_num:
    dasom += 1
    l[0] -= 1
    count += 1
    
    max_num = max(l)
    if l[0] < max_num:
        l.sort(reverse=True)

print(count)