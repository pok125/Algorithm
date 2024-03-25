n = int(input())

zero_count = 0
neg_group = []
positive_group = []
input_num = 0
for i in range(n):
    input_num = int(input())
    if input_num < 0:
        neg_group.append(input_num)
    elif input_num == 0:
        zero_count += 1
    else:
        positive_group.append(input_num)

one_count = positive_group.count(1)
positive_group = sorted(filter(lambda x:x!=1, positive_group), reverse=True)
neg_group.sort()

neg_len = len(neg_group)
positive_len = len(positive_group)

l = [neg_group[i] * neg_group[i + 1] for i in range(0, neg_len - 1, 2)]
l += [positive_group[i] * positive_group[i + 1] for i in range(0, positive_len - 1, 2)]

if neg_len % 2 != 0 and zero_count == 0:
    l.append(neg_group[neg_len - 1])
if positive_len % 2 != 0:
    l.append(positive_group[positive_len - 1])

result = sum(l) if l else 0
result += 1 * one_count
print(result)

# 다른 코드
import sys
N = int(sys.stdin.readline())
minus = []
plus = []
flag_zero = False
hap_one = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        minus.append(num)
    else:
        if num == 0:
            flag_zero = True
            continue
        elif num == 1:
            hap_one += 1
            continue

        plus.append(num)

minus.sort()
plus.sort()
answer = 0
if len(minus) % 2 == 0:
    answer += sum(map(lambda x:x[0]*x[1], zip(minus[::2], minus[1::2])))
else:
    temp = minus.pop()
    if flag_zero:
        temp = 0
    answer += temp
    answer += sum(map(lambda x:x[0]*x[1], zip(minus[::2], minus[1::2])))

if len(plus) % 2 == 0:
    answer += sum(map(lambda x:x[0]*x[1], zip(plus[::2], plus[1::2])))
else:
    temp = plus.pop(0)
    answer += temp
    answer += sum(map(lambda x:x[0]*x[1], zip(plus[::2], plus[1::2])))

if hap_one:
    answer += hap_one
print(answer)
