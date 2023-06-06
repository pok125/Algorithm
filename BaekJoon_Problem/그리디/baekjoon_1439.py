s = input()
count = 0
temp = ['0', '1']
if s[0] == '1':
    temp = ['1', '0']
for i in range(len(s) - 1):
    if s[i] == temp[0] and s[i + 1] == temp[1]:
        count += 1
print(count)