changes = [500, 100, 50, 10, 5, 1]
input_money = int(input())
money = 1000 - input_money

count = 0
for i in changes:
    count += money // i
    money %= i

print(count)
