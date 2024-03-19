num = 1
answer = []
while True:
    string = input()
    if string == "0 0 0":
        break
    
    result = 0
    L, P, V = map(int, string.split(" "))

    result = V // P * L
    rest = V % P
    if rest > L:
        result += L
    else:
        result += rest

    answer.append(f"Case {num}: {result}")
    num += 1

for i in answer:
    print(i)
