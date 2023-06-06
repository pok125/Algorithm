peple_count = int(input())
input_string = input().split(' ')
l = [int(i) for i in input_string]
l.sort()

result = 0
pre =0
for i in l:
    pre += i
    result += pre

print(result)