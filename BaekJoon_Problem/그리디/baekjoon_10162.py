temperature = int(input())
times = [300, 60, 10]

answer = []
for time in times:
    answer.append(str(temperature // time))
    temperature %= time

if temperature != 0:
    print(-1)
else:
    print(str.join(" ", answer))