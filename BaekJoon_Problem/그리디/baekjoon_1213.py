from collections import Counter

input_string = input()
c = Counter(input_string)
sort_key = sorted(c)
l = [i for i in sort_key if c[i] % 2 != 0]

if len(l) > 1:
    print('I\'m Sorry Hansoo')
else:
    result = ''
    s = ''
    mid_char = l.pop(0) if l else ''
    for i in sort_key:
        s += i * (c[i] // 2)
    result = s + mid_char + s[::-1]
    print(result)