N = int(input())
move_dir = input().split(" ")

start_pos = [1, 1]

for dir in move_dir:
    x, y = 0, 0
    match dir:
        case 'L':
            y = -1
        case 'R':
            y = 1
        case 'U':
            x = -1
        case 'D':
            x = 1
    next_posx = start_pos[0] + x
    next_posy = start_pos[1] + y
    if next_posx > N or next_posx <= 0 or next_posy <= 0 or next_posy > N:
        continue

    start_pos[0] += x
    start_pos[1] += y

print(start_pos)