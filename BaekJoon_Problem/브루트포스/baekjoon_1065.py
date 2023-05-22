n = int(input())
result = 0
if n < 100:
    result = n
else:
    flag = True
    result = 99
    for i in range(100, n + 1):
        flag = True
        string = str(i)
        gap = int(string[1]) - int(string[0])
        for j in range(1, len(string) - 1):
            if int(string[j + 1]) - int(string[j]) != gap:
                flag = False
                break
        if flag:
            result += 1

print(result)