import sys
A, B = map(int, sys.stdin.readline().split(" "))

answer = 1

flag = False
while B > A:
    if B % 2 == 0:
        B = B // 2
        answer += 1
    elif str(B)[-1] == "1":
        B = B // 10
        answer += 1
    else:
        flag = True
        break

answer = -1 if B != A or flag else answer
print(answer)