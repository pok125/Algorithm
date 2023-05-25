import heapq
import sys

n = int(input())

l = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
l.sort(key=lambda x:(x[0], x[1]))

heap = []
start, end = l.pop(0)
heapq.heappush(heap, [end, start])
for start, end in l:
    if start < heap[0][0]:
        heapq.heappush(heap, [end, start])
    else:
        heapq.heappushpop(heap, [end, start])

print(len(heap))