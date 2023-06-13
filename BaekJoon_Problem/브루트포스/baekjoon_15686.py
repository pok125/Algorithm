def cal(store):
    result = 0
    ditance = float("inf")
    for hi, hj in pos_home:
        ditance = float("inf")
        for si, sj in store:
            ditance = min(ditance, abs(hi-si) + abs(hj-sj))
        result += ditance
    return result

def solving(count, l):
    if count == len(pos_store):
        if len(l) == m:
            selected_result.append(cal(l))
        return
    
    solving(count + 1, l + [pos_store[count]])
    solving(count + 1, l)
            
n, m = map(int, input().split(" "))
street = [list(map(int, input().split(" "))) for _ in range(n)]

pos_home = []
pos_store = []
selected_result = []
for i in range(0, n):
    for j in range(0, n):
        if street[i][j] == 1:
            pos_home.append((i , j))
        elif street[i][j] == 2:
            pos_store.append((i, j))

solving(0, [])
print(min(selected_result))

