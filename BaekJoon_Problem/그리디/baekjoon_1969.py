import sys

N, M = map(int, sys.stdin.readline().split(" "))
dnas = [sys.stdin.readline().rstrip() for _ in range(N)]
S = ""
for i in range(M):
    h_dic = {"A":0, "C":0, "G":0, "T":0}
    for j in range(N):
        h = dnas[j][i]
        h_dic[h] += 1
    
    sorted_list = sorted(h_dic.items(), key=lambda x:x[0])
    selected_h = ""
    max_v = 0
    for k, v in sorted_list:
        if max_v < v:
            max_v = v
            selected_h = k

    S += selected_h
print(S)

hap = 0
for dna in dnas:
    for i, h in enumerate(dna):
        if h != S[i]:
            hap += 1
print(hap)