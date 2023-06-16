import itertools

l = [int(input()) for _ in range(9)]
# 풀이 1
ll = list(itertools.combinations(l, 7))

result = list(filter(lambda x:sum(x) == 100, ll))
for i in sorted(result[0]):
    print(i)
# 풀이 2
def my_combination(n, m, selected):
    if n == 9:
        if len(selected) == m:
            result.append(selected)
        return
    
    my_combination(n + 1, m, selected + [l[n]])
    my_combination(n + 1, m, selected)

result = []
my_combination(0, 7, [])
for i in result:
    if sum(i) == 100:
        answer = sorted(i)
        break

print(answer)