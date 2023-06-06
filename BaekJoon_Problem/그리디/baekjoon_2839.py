# solusion 1
_input = int(input())
temp = 0
count =0
for i in range(_input // 5 , -1, -1):
    while temp < _input:
        temp = count * 3 + 5 * i
        count += 1
    if temp == _input:
        count += i
        break
    count = 0
    temp = 0

print(count - 1)
# solusion 2
n = int(input())
count = 0
while True:
    if n % 5 == 0:
        count += n // 5
        break
    n -= 3
    count += 1

    if n < 0:
        count = -1
        break
print(count)
