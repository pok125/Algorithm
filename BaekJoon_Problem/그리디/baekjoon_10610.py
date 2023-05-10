from collections import Counter
n = input()
result = '-1'
if '0' not in n:
    print(result)
else:
    result = ''
    c = Counter(n)
    l = sorted(c, reverse=True)
    for i in l:
        result += (i * c[i])
    
    print(result)