l = ['a', 'b', 'c', 'd']
length = len(l)
rec_output = []

def custom_permutation(level, letters):
    if level == length:
        rec_output.append(letters)
        return
    
    # 사용된 문자 빼기
    for i in l:
        if i not in letters:
            custom_permutation(level + 1, letters + i)
    return

custom_permutation(0, '')
print(rec_output)