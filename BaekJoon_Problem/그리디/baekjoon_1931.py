meeting_count = int(input())
time_list = [list(map(int, input().split(' '))) for i in range(meeting_count)]

time_list.sort(key=lambda x:(x[1], x[0]))

end_time = time_list.pop(0)[1]
count = 1
for i in time_list:
    if end_time <= i[0]:
        end_time = i[1]
        count += 1

print(count)