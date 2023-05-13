input_string = input().split(' ')
buy_count = int(input_string[0])
product_count = int(input_string[1])
package_prices = []
per_prices = []

for i in range(product_count):
    input_string = input().split(' ')
    package_prices.append(int(input_string[0]))
    per_prices.append(int(input_string[1]))

min_package_price = min(package_prices)
min_per_price = min(per_prices)

result = 0
selected_count = 0
selected_price = 0
temp = 0
while buy_count > 0:
    selected_count = 6 if buy_count >= 6 else buy_count
    temp = min_per_price * selected_count
    selected_price = min_package_price if min_package_price < temp else temp

    result += selected_price
    buy_count -= selected_count
  
print(result)