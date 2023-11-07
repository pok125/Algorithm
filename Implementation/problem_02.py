end_hour = int(input())
include_three_count_in_60 = 15
include_three_count_in_seconds = 60 * include_three_count_in_60
include_three_count_in_minut = (60 - include_three_count_in_60) * include_three_count_in_60
total_count = include_three_count_in_seconds + include_three_count_in_minut
answer = 0
for hour in range(end_hour + 1):
    if '3' in str(hour):
        answer += 3600
    else:
        answer += total_count
print(answer)
