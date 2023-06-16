import heapq
import sys

n = int(input())
nums = [int(sys.stdin.readline()) for i in range(n)]

l = []
answer = []
temp = 0
for i in nums:
    if i == 0:
        temp = heapq.heappop(l) if l else 0
        answer.append(temp)
    else:
        heapq.heappush(l, i)

for i in answer:
    print(i)