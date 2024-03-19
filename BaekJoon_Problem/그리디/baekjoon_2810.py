peple_count = int(input())
seats = input()
cupholder = 2
seat_count = len(seats)
iscuple = False
for i in range(seat_count - 1):
    if seats[i] == "S":
        cupholder += 1
    else:
        if iscuple:
            cupholder += 1
            iscuple = False
        else:
            iscuple = True

result = cupholder if peple_count > cupholder else peple_count
print(result)
