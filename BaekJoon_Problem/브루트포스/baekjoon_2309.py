import itertools

l = [int(input()) for _ in range(9)]
ll = list(itertools.combinations(l, 7))

result = list(filter(lambda x:sum(x) == 100, ll))
for i in sorted(result[0]):
    print(i)