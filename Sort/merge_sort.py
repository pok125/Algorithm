def merge_sort(l):
    lengh = len(l)
    if lengh <= 1:
        return l
    # left
    half_len = lengh // 2
    l1 = merge_sort(l[:half_len])
    # right
    l2 = merge_sort(l[half_len:])
    
    reseult = []
    while l1 and l2:
        if(l1[0] < l2[0]):
            reseult.append(l1.pop(0))
        else:
            reseult.append(l2.pop(0))

    for i in l1:
        reseult.append(i)
    for i in l2:
        reseult.append(i)

    return reseult

l = [6, -8, 1, 12, 8, 15, 7, -7]
print(merge_sort(l))

