day_list = [3, 5, 1, 1, 2, 4, 2]
price_list = [10, 20, 10, 20, 15, 40, 200]
n = 7

result = []
# 완전 탐색적 풀이
def solution(index, price):
    if index >= n:
        result.append(price)
        return
    
    if index + day_list[index] <= n:
        solution(index + day_list[index], price + price_list[index])
    
    solution(index + 1, price)

# dp 풀이
def dp_solution(day):
    l = [0] * (day + 1)

    required_days =0
    max_price = 0
    for i in range(day - 1, -1, -1):
        required_days = day_list[i]
        max_price = l[i + 1]

        if required_days + i <= day:
            # 이전 최대값과 내 현재 값 + 소요되는 시간 후의 값
            max_price = max(max_price, price_list[i] + l[required_days + i])

        l[i] = max_price
    
    return l

print(dp_solution(7))