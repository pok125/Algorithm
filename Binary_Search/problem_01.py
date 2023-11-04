# 부품 찾기
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Util.decorator import check_time 
# 이진 탐색 풀이
@check_time
def binary_search(num_list, find_list):
    num_list.sort()
    start_index = 0
    end_index = N - 1
    mid_index = end_index // 2
    answer = []

    for num in find_list:
        start_index = 0
        end_index = N - 1
        flag = False

        while start_index <= end_index:
            mid_index = (start_index + end_index) // 2

            if num_list[mid_index] > num:
                end_index = mid_index - 1
            elif num_list[mid_index] < num:
                start_index = mid_index + 1
            else:
                answer.append("yes")
                flag = True
                break

        if flag == False:
            answer.append("no")

    return answer

# 계수 정렬 풀이
@check_time
def counting_sort(max_length, num_list, find_list):
    arr = [0] * (max_length + 1)
    answer = []
    for i in set(num_list):
        arr[i] += 1
    for i in find_list:
        if arr[i] == 0:
            answer.append("no")
        else:
            answer.append("yes")

    return answer

# Counter 풀이
@check_time
def by_counter(num_list, find_list):
    from collections import Counter

    c = Counter(set(num_list))
    answer = []
    for i in find_list:
        if c.get(i):
            answer.append("yes")
        else:
            answer.append("no")

    return answer

N = int(input())
num_list = list(map(int, input().split(" ")))
M = int(input())
find_list = list(map(int, input().split(" ")))

r1 = binary_search(num_list, find_list)
r2 = counting_sort(1000000, num_list, find_list)
r3 = by_counter(num_list, find_list)

print(r1, r2, r3)