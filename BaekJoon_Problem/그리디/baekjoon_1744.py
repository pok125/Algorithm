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