N = int(input())
borad = [list(map(int, input().split(" "))) for _ in range(N)]

# 거쳐가는 노드
for k in range(N):
    # 출발 노드
    for i in range(N):
        # 도착 노드
        for j in range(N):
            if borad[i][k] == 1 and borad[k][j] == 1:
                borad[i][j] = 1

for i in range(N):
    for j in range(N):
        print(borad[i][j], end=" ")
    print()
