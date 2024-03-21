import sys

test_case = int(sys.stdin.readline())
answer = []
for i in range(test_case):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split(" ")))
    cal = []
    result = 0
    max_price = 0
    for price in prices[::-1]:
        if max_price < price:
            max_price = price
        else:
            temp = max_price - price
            result += temp
    answer.append(result)

for i in answer:
    print(i)