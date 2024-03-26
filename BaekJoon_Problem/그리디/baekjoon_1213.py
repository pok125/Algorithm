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

# 다른 코드
import sys
from collections import Counter

string = sys.stdin.readline().rstrip()
c = Counter(string)
sorted_c = sorted(c.items(), key=lambda x:x[0])
temp = []
count = 0
mid_char = ""
answer = ""
flag = False
for key, value in sorted_c:
    if value % 2 != 0:
        count += 1
        mid_char = key

    if count > 1:
        flag = True
        break
    
    temp.extend(key * (value // 2))

answer = ''.join(temp) + mid_char + ''.join(temp[::-1])
answer = answer if flag is False else "I'm Sorry Hansoo"
print(answer)    