n = int(input())
l = [list(map(int, input().split(' '))) for _ in range(n)]

result = ''
count = 0
for i in l:
    count = len(list(filter(lambda x:x[0]>i[0] and x[1]>i[1], l))) + 1
    result += str(count) + ' '
print(result.strip())