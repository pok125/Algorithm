input_list = list(map(int, input().split(' ')))
coin_list = [int(input()) for i in range(input_list[0])]

result = 0
money = input_list[1]
for i in coin_list[::-1]:
    result += money // i
    money %= i
print(result)
