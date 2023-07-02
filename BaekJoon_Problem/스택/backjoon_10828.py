stack = []
answer = []
n = int(input())
for _ in range(n):
    inputs = input().split(" ")

    match inputs[0]:
        case "push":
            stack.append(inputs[1])
        case "pop":
            value = stack.pop() if stack else -1
            answer.append(value)
        case "size":
            answer.append(len(stack))
        case "empty":
            value = 0 if stack else 1
            answer.append(value)
        case "top":
            value = stack[len(stack) - 1] if stack else -1
            answer.append(value)

for i in answer:
    print(i)
            