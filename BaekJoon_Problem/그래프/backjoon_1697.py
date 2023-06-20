temp_list = []
n, m = map(int, input().split(" "))
# 시간 초과 풀이
# pre_list = []
# next_list = []
# temp_list.append(n)
# next_list.append(n)
# count = 0
# while m not in temp_list:
#     pre_list = next_list.copy()
#     next_list.clear()
#     for i in pre_list:
#         if i - 1 > 0 and i - 1 not in temp_list:
#             next_list.append(i - 1)
#             temp_list.append(i - 1)
#         if i + 1 < m and i + 1 not in temp_list:
#             next_list.append(i + 1)
#             temp_list.append(i + 1)
#         if i * 2 < m and i * 2 not in temp_list:
#             next_list.append(i * 2)
#             temp_list.append(i * 1)
    
#     count += 1
queue = []
size = m if m >= n else n
visited = [0] * (2 * size + 1)
length = len(visited)
queue.append(n)
while queue:
    cur_pos = queue.pop(0)
    if cur_pos == m:
        break

    for i in (cur_pos - 1, cur_pos + 1, cur_pos * 2):
        if i >= length or i < 0:
            continue
        if visited[i] != 0:
            continue
        queue.append(i)
        visited[i] = visited[cur_pos] + 1

print(visited[m])