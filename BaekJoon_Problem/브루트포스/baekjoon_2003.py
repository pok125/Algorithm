n, m = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

front, end = 0, 0
hap = 0
count = 0
while end < n:
    hap += l[end]
    if hap >= m:
        if hap == m:
            count += 1
        front += 1
        hap = 0
        end = front
        continue
    
    end += 1

print(count)