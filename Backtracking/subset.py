'''
선택 가능한 경우의 수 (decision space)가 있을 때 까지
탐색 한다.
'''

# subset 문자들이 주어 졌을 때, 만들 수 있는 모든 문자열
# 풀이: 문자를 선택하는 것과 하지않는 것의 decision space 구성

l = ['a', 'b', 'c']
length = len(l)
rec_output = []
iter_output = []

# 재귀로 구현
def recursion_solve(index, letter):
    if index == length:
        rec_output.append(letter)
        return

    char = l[index]

    # 문자를 선택
    recursion_solve(index + 1, letter + char)
    # 선택 하지 않음
    recursion_solve(index + 1, letter)
    return

# while 구현
def iterative_solve(index, letter):
    s = [(index, letter)]

    while s:
        idx, cur_letter = s.pop()
        if idx == length:
            iter_output.append(cur_letter)
            continue

        char = l[idx]

        s.append((idx + 1, cur_letter + char))
        s.append((idx + 1, cur_letter))

recursion_solve(0, '')
iterative_solve(0, '')

print(f'recursion {rec_output}')
print(f'iterative {iter_output}')