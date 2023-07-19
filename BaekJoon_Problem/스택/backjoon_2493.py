import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split(" ")))
stack = []
result = []
for i in range(len(l)):

    if not stack:
        stack.append(i)
        result.append(0)
    else:
        while stack and l[stack[-1]] < l[i]:
            stack.pop()
        
        if not stack:
            result.append(0)
        else:
            result.append(stack[-1] + 1)

        stack.append(i)

print(*result)