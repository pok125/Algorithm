input_string = input()
stack = []
answer = []
priority = {
    '+': 1,        
    '-': 1, 
    '*': 2, 
    '/': 2
}

temp = 1
last_index = -1
for char in input_string:
    if char == '+' or char == '-' or char == '*' or char == '/':
        cur_char_priority = priority[char] * temp
        
        while stack and stack[last_index][1] >= cur_char_priority:
            answer.append(stack[last_index][0])
            stack.pop()
            last_index -= 1
        
        stack.append((char, cur_char_priority))
        last_index += 1
    elif char == '(':
        temp *= 10
    elif char == ')':
        temp //= 10
    else:
        answer.append(char)

while stack:
    answer.append(stack.pop()[0])

print(str.join('', answer))
