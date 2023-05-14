input_string = input().split(' ')
n = int(input_string[0])
tape_len = int(input_string[1])

input_string = input().split(' ')
l = sorted(map(int, input_string))

end = 0
count = 0
for i in l:
    if end < i:
        end = i + tape_len - 1
        count += 1

print(count)