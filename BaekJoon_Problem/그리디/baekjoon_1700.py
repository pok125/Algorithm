import sys

N, K = map(int, sys.stdin.readline().split(" "))
elecs = list(map(int, sys.stdin.readline().split(" ")))
usings = []
count = 0

if N >= K:
    print(count)
else:
    for i in range(K):
        next_elec = elecs[i]
        if next_elec in usings:
            continue
        if len(usings) < N:
            usings.append(next_elec)
            continue
        
        priority = []
        temp = elecs[i:]
        for elec in usings:
            if elec in temp:
                priority.append(temp.index(elec))
            else:
                priority.append(1000)
        
        remove_target = priority.index(max(priority))
        usings.pop(remove_target)
        usings.append(next_elec)
        count += 1

    print(count)