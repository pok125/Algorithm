import sys

N = int(sys.stdin.readline())
lengths = list(map(int, sys.stdin.readline().split(" ")))
prices = list(map(int, sys.stdin.readline().split(" ")))

total_price = 0
cur_min_price = prices[0]
length_hap = 0

for i in range(N - 1):
    price = prices[i]
    if cur_min_price > price:
        total_price += (cur_min_price * length_hap)
        cur_min_price = price
        length_hap = lengths[i]
    else:
        length_hap += lengths[i]

total_price += cur_min_price * length_hap

print(total_price)

for i in range(N - 1):
    if cur_min_price > prices[i]:
        cur_min_price = prices[i]
    total_price += cur_min_price * lengths[i]

print(total_price)