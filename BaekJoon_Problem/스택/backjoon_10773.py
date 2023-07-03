n = int(input())
l = [int(input()) for _ in range(n)]

stack = []
for num in l:
    if stack and num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))