n = int(input())

answer = []
stack = []
l = [input() for _ in range(n)]
flag = False
for i in l:
    flag = False
    stack.clear()
    for j in i:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                flag = True
                break

    if len(stack) > 0 or flag:
        answer.append("NO")
    else:
        answer.append("YES")

for i in answer:
    print(i)