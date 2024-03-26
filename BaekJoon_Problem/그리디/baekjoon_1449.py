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

# 다른 풀이
import sys
N, tape = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))

l.sort()
count = 1
start = l[0]

for i in range(1, N):
    if tape <= l[i] - start:
        count += 1
        start = l[i]
print(count)
