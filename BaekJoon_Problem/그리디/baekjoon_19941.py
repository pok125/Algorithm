import sys

def check_range(peple_index):
    for i in range(peple_index - K, (peple_index + K) + 1):
        if i < 0 or i >= N:
            continue
        if l[i] == "H" and ll[i] == 0:
            return i
    return None
        

N, K = map(int, sys.stdin.readline().split(" "))
l = sys.stdin.readline().rstrip()
ll = [0 for _ in range(N)]
count = 0
for i in range(N):
    if l[i] == "P":
        result = check_range(i)
        if result is not None:
            ll[result] = 1
            count += 1

print(count)         
