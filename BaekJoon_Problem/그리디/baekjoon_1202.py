import sys, heapq

N, K = map(int, sys.stdin.readline().split(" "))
jewels = [list(map(int, sys.stdin.readline().split(" ")))for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

heapq.heapify(jewels)
bags.sort()

selects = []
answer = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        w, p = heapq.heappop(jewels)
        heapq.heappush(selects, -p)

    if selects:
        answer -= heapq.heappop(selects)
print(answer)