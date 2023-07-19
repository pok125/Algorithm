string = input()
bomb_str = input()

# 시간 초과
# while bomb_str in string:
#     string = string.replace(bomb_str, '')

# string = string if string else 'FRULA'

stack = []
bomb_str_len = len(bomb_str)
result = ''
temp = ''
for i in string:
    stack.append(i)

    if stack[-1] == bomb_str[-1]:
        temp = str.join('', stack[(-1 * bomb_str_len):])
        if temp == bomb_str:
            for _ in range(bomb_str_len):
                stack.pop()

result = str.join('', stack) if stack else 'FRULA'
print(result)