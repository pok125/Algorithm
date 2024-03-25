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

# 다른 코드
import sys

N = int(sys.stdin.readline())
alphabet_value = {}
words = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in words:
    length = len(word)
    for i, char in enumerate(word, 1):
        alphabet_value[char] = alphabet_value.get(char, 0) + (10 ** (length - i))

count = 9
for key, value in sorted(alphabet_value.items(), key = lambda x:x[1], reverse=True):
    alphabet_value[key] = count
    count -= 1

total_hap = 0
for word in words:
    length = len(word)
    num = 0
    for i, char in enumerate(word, start=1):
        num += alphabet_value[char] * (10 ** (length -i))
    total_hap += num

print(total_hap)