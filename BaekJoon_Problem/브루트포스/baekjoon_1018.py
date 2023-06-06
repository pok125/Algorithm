def check_board_count(board, x, y, color):
    start_char = color
    char_dict = {'B': 'W', 'W': 'B'}
    cur_char = ''
    count = 0
    for i in range(x, x + 8):
        cur_char = start_char
        for j in range(y, y + 8):
            if board[i][j] != cur_char:
                count += 1
            cur_char = char_dict[cur_char]
        start_char = char_dict[start_char]
    return count

n, m = input().split(' ')
n, m = int(n), int(m)
board = [input() for _ in range(n)]

startX = 0
startY = 0
result = []
while True:
    if startX + 8 > n:
        break
    
    result.append(check_board_count(board, startX, startY, 'B'))
    result.append(check_board_count(board, startX, startY, 'W'))
    startY += 1
    if startX + 8 <= n and startY + 8 > m:
        startX += 1
        startY = 0
print(min(result))