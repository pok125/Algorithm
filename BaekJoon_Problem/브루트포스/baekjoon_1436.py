n = int(input())
count = 1
result = 666
while count < n:
    result += 1
    if '666' in str(result):
        count += 1

print(result)
