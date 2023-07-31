from collections import deque

N, L, R = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]

queue = deque()

total_sum = 0
tpos = [0, 0]
count = 0
while count <= 2000:
    visited = [[0] * N for _ in range(N)]
    
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            # 연합 체크
            queue.append((i , j))
            visited[i][j] = 1
            temp_list = [(i, j)]
            
            total_sum = board[i][j]

            while queue:
                pos = queue.popleft()

                for check in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    tpos[0], tpos[1] = pos[0] + check[0], pos[1] + check[1]
                    if tpos[0] >= N or tpos[0] < 0 or tpos[1] >= N or tpos[1] < 0:
                        continue
                    if visited[tpos[0]][tpos[1]]:
                        continue
                    if L <= abs(board[pos[0]][pos[1]] - board[tpos[0]][tpos[1]]) <= R:
                        queue.append((tpos[0], tpos[1]))
                        visited[tpos[0]][tpos[1]] = 1
                        temp_list.append((tpos[0], tpos[1]))
                        total_sum += board[tpos[0]][tpos[1]]
            
            length = len(temp_list)
            if length > 1:
                flag = True
                for ti, tj in temp_list:
                    board[ti][tj] = total_sum // length
            
    if flag == False:
        break
    count += 1     
print(count)