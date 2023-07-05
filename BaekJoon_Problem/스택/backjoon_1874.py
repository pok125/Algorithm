n = int(input())
l = [int(input()) for _ in range(n)]
num = 1
index = 0
stack = []
answer = []
while index < n:
    
    if l[index] >= num:
        if num <= n:
            answer.append('+')
            stack.append(num)
            num += 1
    
    if l[index] < num:
        if l[index] != stack.pop():
            answer.clear()
            answer.append('NO')
            break
        answer.append('-')
        index += 1

for i in answer:
    print(i)