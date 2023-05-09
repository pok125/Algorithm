test_case = int(input())
result = []
for _ in range(test_case):
    people_count = int(input())
    l = []
    first_list = []
    second_list = []
    temp = []
    isdouble_first = False
    for _ in range(people_count):
        l = list(map(int, input().split(' ')))
        if l[0] == 1 and l[1] == 1:
            temp.append(l)
            isdouble_first = True
        if not(isdouble_first):
            if l[0] == 1 or l[1] == 1:
                first_list.append(l)
            if l[0] == 2 or l[1] == 2:
                second_list.append(l)
    
    if not(isdouble_first):
        first_list.sort(key=lambda x:x[0])
        second_list.sort(key=lambda x:x[0])
        for i in first_list:
            temp.append(i)
        if second_list[0][1] < first_list[0][1]:
            temp.append(i)
        if second_list[1][0] < first_list[1][0]:
            temp.append(i)
        result.append(len(temp))
   
for i in result:
    print(i)