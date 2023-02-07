def move_all_zeros(arr: list):
    zero_count = 0
    output = list()
    for i in arr:
        if i > 0:
            output.append(i)
        else:
            zero_count += 1

    while zero_count > 0:
        output.append(0)
        zero_count -= 1
    print(zero_count)
    return output


print(move_all_zeros([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]))
