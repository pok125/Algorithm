num1, num2 = input().split(" ")

max_num = int(num1.replace("5", "6")) + int(num2.replace("5", "6"))
min_num = int(num1.replace("6", "5")) + int(num2.replace("6", "5"))
print(f"{min_num} {max_num}")