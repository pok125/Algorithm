# 수정 필요
from collections import Counter

input_strings = input().split(' ')
n = int(input_strings[0])
k = int(input_strings[1])

l = [input() for _ in range(n)]
jewel_infos = [list(map(int, i.split())) for i in l]
bag_weights = [int(input()) for _ in range(k)]

jewel_infos.sort(key=lambda x:x[1], reverse=True)
bag_weights.sort()
c = Counter(bag_weights)
print(c)
# result = 0
# cur_bag = 0
# while bag_weights:
#     cur_bag = bag_weights.pop(0)
#     for i in jewel_infos:
#         if cur_bag >= i[0]:
#             result += i[1]
#             jewel_infos.remove(i)
#             break

# print(result)