import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

hap = 0
while len(cards) > 1:
    num = heapq.heappop(cards) + heapq.heappop(cards)
    hap += num
    heapq.heappush(cards, num)

print(hap)
