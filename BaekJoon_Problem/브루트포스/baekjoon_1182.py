N, hap = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
count = 0
def solution(index, cur_hap, length):
    global count
    
    if index == N:
        if cur_hap == hap and length > 0:
            count += 1
        return
    
    num = nums[index]
    cur_hap += num
    index += 1
    length += 1
    solution(index, cur_hap, length)
    cur_hap -= num
    length -= 1
    solution(index, cur_hap, length)

solution(0, 0, 0)
print(count)