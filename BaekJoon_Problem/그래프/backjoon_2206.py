from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    pos = [0, 0]
    while queue:
        cur_pos = queue.popleft()
        crashed = cur_pos[2]

        if cur_pos[0] == N - 1 and cur_pos[1] == M - 1:
            return visited[N - 1][M - 1][crashed]

        for check in check_pos:
            pos[0] = cur_pos[0] + check[0]
            pos[1] = cur_pos[1] + check[1]

            if pos[0] >= N or pos[0] < 0 or pos[1] >= M or pos[1] < 0:
                continue
            if visited[pos[0]][pos[1]][crashed] != 0:
                continue
            # 벽일 때
            if board[pos[0]][pos[1]] == "1":
                # 벽을 이미 부셨다면
                if crashed == 1:
                    continue

                queue.append((pos[0], pos[1], 1))
                visited[pos[0]][pos[1]][1] = visited[cur_pos[0]][cur_pos[1]][crashed] + 1
            else:
                queue.append((pos[0], pos[1], crashed))
                visited[pos[0]][pos[1]][crashed] = visited[cur_pos[0]][cur_pos[1]][crashed] + 1

    return -1


N, M = map(int, input().split(" "))
check_pos = [(0, -1), (0, 1), (1, 0), (-1, 0)]
board = [input() for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())