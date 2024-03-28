# 시간 초과
import sys
# G = int(sys.stdin.readline())
# P = int(sys.stdin.readline())
# l = [int(sys.stdin.readline()) for _ in range(P)]
# ll = [False] * G

# answer = 0
# for g in l:
#     while g > 0:
#         if ll[g - 1] is False:
#             ll[g - 1] = True
#             answer += 1
#             break
#         g -= 1
    
#     if g <= 0:
#         break

# print(answer)

# 위으 코드를 Union-find 알고리즘을 통해 시간복잡도를 줄임
def find(gate_num):
    if gates[gate_num] == gate_num:
        return gate_num
    gates[gate_num] = find(gates[gate_num])
    return gates[gate_num]

def union(gate1, gate2):
    gates[find(gate2)] = find(gate1)


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(P)]
gates = [i for i in range(G + 1)]
answer = 0
for gate_num in l:
    if find(gate_num) == 0:
        break
    union(find(gate_num) - 1, find(gate_num))
    answer += 1

print(answer)