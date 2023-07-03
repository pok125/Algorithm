def bfs(start_pos):
    
    queue = []
    queue.append(start_pos)
    temp_pos = [0, 0]
    visited[start_pos[0]][start_pos[1]] = 1
    
    while queue:
        cur_pos = queue.pop(0)

        for check in check_pos:
            temp_pos[0] = cur_pos[0] + check[0]
            temp_pos[1] = cur_pos[1] + check[1]

            if temp_pos[0] >= N or temp_pos[0] < 0 or temp_pos[1] >= N or temp_pos[1] < 0:
                continue
            if visited[temp_pos[0]][temp_pos[1]] != 0:
                continue

            queue.append((temp_pos[0], temp_pos[1]))
            visited[temp_pos[0]][temp_pos[1]] = visited[cur_pos[0]][cur_pos[1]] + 1

test_case = int(input())
answer = []
check_pos = [(2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, 1), (-2, -1)]

for _ in range(test_case):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start_pos = tuple(map(int, input().split(" ")))
    end_pos = tuple(map(int, input().split(" ")))
    bfs(start_pos)
    answer.append(visited[end_pos[0]][end_pos[1]] - 1)

for i in answer:
    print(i)