import sys

def find_parents(n):
    if parents[n] == n:
        return n
    parents[n] = find_parents(parents[n])
    return parents[n]

def union_parents(n1, n2):
    pn1 = find_parents(n1)
    pn2 = find_parents(n2)
    
    if pn1 == pn2:
        return 0
    
    if pn1 < pn2:
        parents[pn2] = pn1
    else:
        parents[pn1] = pn2

V, E = map(int, sys.stdin.readline().split(" "))
infos = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(E)]
ordered_infos = sorted(infos, key=lambda x:x[2])

parents = [i for i in range(V + 1)]
hap = 0
for v1, v2, w in ordered_infos:
    if union_parents(v1, v2) != 0:
        hap += w

print(hap)