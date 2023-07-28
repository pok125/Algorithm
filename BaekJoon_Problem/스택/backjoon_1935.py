n = int(input())
string = input()
l = [int(input()) for _ in range(n)]
ll = [ chr(ord('A') + i) for i in range(n)]
value = dict(zip(ll, l))
stack = []

for char in string:
    if char == '*' or char == '/' or char == '+' or char == '-':
        v2 = stack.pop()
        v1 = stack.pop()
        match char:
            case '*':
                stack.append(v1 * v2)
            case '/':
                stack.append(v1 / v2)
            case '+':
                stack.append(v1 + v2)
            case '-':
                stack.append(v1 - v2)
    else:
        stack.append(value[char])

answer = float(stack.pop())
print(f'{answer:.2f}')        