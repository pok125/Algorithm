# 수정 필요
n = int(input())
l = [input() for _ in range(n)]
max_length = len(max(l, key=len))

l = [i.zfill(max_length) for i in l]
l = list(map(list, l))

char_value_dic = {}
cur_char = ''
count = 9
index = 0
for i in range(max_length):
    for j in range(len(l)):
        cur_char = l[j][i]
        if cur_char == '0':
            continue

        if cur_char not in char_value_dic:
            char_value_dic[cur_char] = str(count)
            l[j][i] = str(count)
            count -= 1
        else:
            l[j][i] = char_value_dic[cur_char]

result_list = [int(str.join('', i)) for i in l]
result = sum(result_list)
print(result)