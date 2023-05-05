meeting_count = int(input())
time_list = [list(map(int, input().split(' '))) for i in range(meeting_count)]

time_list.sort(key=lambda x:(x[1], x[0]))
print(time_list)
selected_meeting = time_list[0]
count = 1
for i in time_list:
    if selected_meeting[1] <= i[0]:
        selected_meeting = i
        count += 1

print(count)