input_string = input()
stack = []
temp = []
last_index = -1
for char in input_string:
    if stack:
        if stack[last_index] == '(' and char == ')':
            pass
        elif stack[last_index] == '[' and char == ']':
            pass
    else:
        stack.append(char)
        last_index += 1