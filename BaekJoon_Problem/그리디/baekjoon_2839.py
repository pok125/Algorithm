_input = int(input())
temp = 0
count =0
for i in range(_input // 5 , -1, -1):
    while temp < _input:
        temp = count * 3 + 5 * i
        count += 11
    if temp == _input:
        count += i
        break
    count = 0
    temp = 0

print(count - 1)
