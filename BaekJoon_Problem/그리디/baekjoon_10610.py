n = input()
result = -1
if '0' not in n:
    print(result)
else:
    l = sorted(n, reverse=True)
    temp = 0
    for i in l:
        temp += int(i)
    
    if temp % 3 == 0:
        result = int(str.join('', l))
    print(result)