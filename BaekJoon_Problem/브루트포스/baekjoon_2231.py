n = int(input())
result = 0
temp = 0
for i in range(1, n):
    string = str(i)
    temp = i + sum(map(int, string))
    if temp == n:
        result = i
        break

print(result)