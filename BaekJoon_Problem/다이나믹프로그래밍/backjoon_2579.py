n = int(input())
score = [0] * (n + 3)
l = [0] * (n + 3)
for i in range(n):
    score[i] = int(input())

l[0] = score[0]
l[1] = score[0] + score[1]
l[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, n):
    v1 = l[i - 3] + score[i - 1] + score[i]
    v2 = l[i - 2] + score[i]
    l[i] = max(v1, v2)

print(l[n - 1])