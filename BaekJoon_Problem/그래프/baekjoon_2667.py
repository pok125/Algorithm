# 수정해야함
def bfs():
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1

    pos = [0, 0]
    while queue:
        cur_pos = queue.pop(0)
        
        for i in check_pos:
            pos[0] = cur_pos[0] + i[0]
            pos[1] = cur_pos[1] + i[1]

            if pos[0] >= n or pos[0] < 0 or pos[1] >= m or pos[1] < 0:
                continue
            if board[pos[0]][pos[1]] == "0":
                continue
            if visited[pos[0]][pos[1]]:
                continue
            
            queue.append((pos[0], pos[1]))
            visited[pos[0]][pos[1]] = visited[cur_pos[0]][cur_pos[1]] + 1
        
check_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split(" "))
board = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

bfs()
print(visited[n - 1][m - 1])