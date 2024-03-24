S = int(input())
hap = 0
count = 1
while hap < S:
    hap += count
    count += 1
if hap > S:
    print(count - 2)
else:
    print(count - 1)