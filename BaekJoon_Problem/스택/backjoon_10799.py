s = input()
s = s.replace('()', '.')

stack = []
count = 0
for i in s:
    if i == '(':
        stack.append(i)
    elif i == '.':
        count += len(stack)
    elif i == ')':
        stack.pop()
        count += 1

print(count)