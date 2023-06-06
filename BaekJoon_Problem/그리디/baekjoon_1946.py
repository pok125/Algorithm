import sys

test_case = int(sys.stdin.readline())
result = []

for _ in range(test_case):
    people_count = int(sys.stdin.readline())
    total_list = []
    for _ in range(people_count):
        l = list(map(int, sys.stdin.readline().split(' ')))
        total_list.append(l)

    count = 1
    total_list.sort(key=lambda x:x[0])
    cur_interview_score = total_list.pop(0)[1]
    
    if cur_interview_score != 1:
        for i in total_list:
            if i[1] == 1:
                count += 1
                break
            
            if cur_interview_score > i[1]:
                cur_interview_score = i[1]
                count += 1
    
    result.append(count)

for i in result:
    print(i)