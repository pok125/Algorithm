import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split(" ")))
stack = []
result = []

for i in range(len(l) - 1, -1, -1):
    if not stack:
        stack.append(l[i])
        result.append(-1)
    else:
        while stack and stack[-1] <= l[i]:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        stack.append(l[i])

print(*result[::-1])