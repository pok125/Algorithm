n = int(input())
l = [input() for _ in range(n)]

w_dic = {}
for i in l:
    for j in range(len(i)):
        if i[j] not in w_dic:
            w_dic[i[j]] = 10 ** (len(i) - j - 1)
        else:
            w_dic[i[j]] += 10 ** (len(i) - j - 1)

ll = sorted(w_dic, key=w_dic.get, reverse=True)
count = 9
for i in ll:
    w_dic[i[0]] = str(count)
    count -= 1

result_list = []
s = ''
for i in l:
    s = ''
    for j in i:
        s += w_dic[j]
    result_list.append(s)

print(sum(map(int, result_list)))