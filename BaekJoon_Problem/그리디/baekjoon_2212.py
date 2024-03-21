N = int(input())
K = int(input())

sensors = list(map(int, input().split(" ")))

sensors.sort()
length = []
for i in range(N - 1):
    length.append(sensors[i+1]-sensors[i])

length.sort(reverse=True)
print(sum(length[K-1:]))