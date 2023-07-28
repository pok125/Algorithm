test_case = int(input())
count = 0
for _ in range(test_case):
    string = input()
    stack = []
    last_index = -1
    
    for char in string:
        if stack and stack[last_index] == char:
            stack.pop()
            last_index -= 1
        else:
            stack.append(char)
            last_index += 1
    
    if not(stack):
        count += 1

print(count)