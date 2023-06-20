def bfs(pos):
    global count
    if visited[pos[1]][pos[0]]:
        return
    
    queue = []
    queue.append(pos)
    visited[pos[1]][pos[0]] = 1
    temp_pos = [0, 0]
    count += 1

    while queue:
        cur_pos = queue.pop()

        for i in check_pos:
            temp_pos[0] = cur_pos[0] + i[0]
            temp_pos[1] = cur_pos[1] + i[1]

            if temp_pos[0] >= M or temp_pos[0] < 0 or temp_pos[1] >= N or temp_pos[1] < 0:
                continue
            if board[temp_pos[1]][temp_pos[0]] == 0:
                continue
            if visited[temp_pos[1]][temp_pos[0]]:
                continue

            queue.append((temp_pos[0], temp_pos[1]))
            visited[temp_pos[1]][temp_pos[0]] = 1
    
test_case = int(input())
answer = []
check_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(test_case):
    M, N, K = map(int, input().split(" "))
    count = 0
    board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    exist_pos = [tuple(map(int, input().split(" "))) for _ in range(K)]

    for i in exist_pos:
        board[i[1]][i[0]] = 1
    
    for i in exist_pos:
        bfs(i)
    answer.append(count)
for i in answer:
    print(i)