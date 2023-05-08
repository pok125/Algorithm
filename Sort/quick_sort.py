def quick_sort(l):
    if len(l) <= 1:
        return l
    
    half_len = len(l) // 2
    pivot = l.pop(half_len)
    left_group = []
    right_group = []
    
    for i in l:
        if i < pivot:
            left_group.append(i)
        else:
            right_group.append(i)

    return quick_sort(left_group) + [pivot] + quick_sort(right_group)

l = [6, -8, 1, 12, 8, 15, 7, -7]
print(quick_sort(l))