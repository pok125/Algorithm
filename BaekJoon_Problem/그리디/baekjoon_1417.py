# import sys

# N = int(sys.stdin.readline())
# l = [int(sys.stdin.readline()) for _ in (range(N))]

# dasom = l.pop(0)
# l.sort(reverse=True)

# count = 0
# max_num = l[0] if l else 0
# while l and dasom <= max_num:
#     dasom += 1
#     l[0] -= 1
#     count += 1
    
#     max_num = max(l)
#     if l[0] < max_num:
#         l.sort(reverse=True)

# print(count)

# 우선순위 큐 풀이
import sys, heapq

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) * -1 for _ in (range(N))]

dasom = l.pop(0) * -1
heapq.heapify(l)
count = 0

while l and dasom <= (l[0] * -1):
    heapq.heappushpop(l, l[0] + 1)
    dasom += 1
    count += 1

print(count)