import heapq
# 1. 현재 상어 위치 기준 먹을 수 있는 물고기 위치 찾기
# 2. 찾은 물고기 위치들 중에 조건이 부합되는 위치로 상어 위치 이동
# 3. 이동한 위치 기준으로 다시 물고기 탐색

def find_fish(shark_pos):
    queue = []
    fish_list = []
    visited = [[0] * N for _ in range(N)]    
    queue.append(shark_pos)
    temp = [0, 0]
    
    while queue:
        cur_pos = queue.pop(0)
        
        for check in check_dir:
            temp[0] = cur_pos[0] + check[0]
            temp[1] = cur_pos[1] + check[1]

            if temp[0] >= N or temp[0] < 0 or temp[1] >= N or temp[1] < 0:
                continue
            if visited[temp[0]][temp[1]] != 0:
                continue
            if board[temp[0]][temp[1]] > shark_size :
                continue
            
            queue.append((temp[0], temp[1ㅎ]))
            visited[temp[0]][temp[1]] = visited[cur_pos[0]][cur_pos[1]] + 1    
            # 먹을 수 있는 물고기라면
            if board[temp[0]][temp[1]] != 0 and board[temp[0]][temp[1]] < shark_size:
                distance = visited[temp[0]][temp[1]]
                heapq.heappush(fish_list, (distance, temp[0], temp[1]))

    # 먹을 수 있는 물고기가 있다면
    if fish_list:
        return heapq.heappop(fish_list)
        
    return ()

N = int(input())
board = [list(map(int, input().split(" "))) for _ in range(N)]

start_pos = [0, 0]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            start_pos[0], start_pos[1] = i, j
            break

shark_size = 2
eating_count = 0
total_time = 0
check_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while True:
    fish_pos = find_fish(start_pos)

    # 먹을 수 있는 물고기 위치
    if fish_pos:
        total_time += fish_pos[0]
        eating_count += 1
        if eating_count == shark_size:
            shark_size += 1
            eating_count = 0

        # 상어 위치 옮기기
        board[start_pos[0]][start_pos[1]] = 0
        board[fish_pos[1]][fish_pos[2]] = 9
        start_pos[0], start_pos[1] = fish_pos[1], fish_pos[2]
    else:
        break
        
print(total_time)