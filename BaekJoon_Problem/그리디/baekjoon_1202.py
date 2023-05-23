import heapq
import sys

input_strings = input().split(' ')
n = int(input_strings[0])
k = int(input_strings[1])

l = [sys.stdin.readline() for _ in range(n)]
jewel_heap = [list(map(int, i.split(' '))) for i in l]
heapq.heapify(jewel_heap)
bag_weights = [int(sys.stdin.readline()) for _ in range(k)]
bag_weights.sort()

result = []
answer = 0
for i in bag_weights:
    while jewel_heap and i >= jewel_heap[0][0]:
        weight, price = heapq.heappop(jewel_heap)
        heapq.heappush(result, -price)
    if result:
        answer -= heapq.heappop(result)
    elif not(jewel_heap):
        break

print(answer)