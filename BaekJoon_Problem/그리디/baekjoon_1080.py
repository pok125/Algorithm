import sys
N, M = map(int, sys.stdin.readline().split(" "))
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def flip(pos):
    x, y = pos
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return -1
    
    return 0

answer = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip((i, j))
            answer += 1

answer = answer if check() == 0 else -1
print(answer)