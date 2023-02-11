def move_zeros_once_two(arr: list):
    zero_count = 0
    once_count = 0
    two_count = 0
    for i in range(len(arr)):
        match arr[i]:

            case 0:
                zero_count += 1

            case 1:
                once_count += 1

            case 2:
                two_count += 1
    i = 0
    while zero_count > 0:
        arr[i] = 0
        zero_count -= 1
        i += 1
    while once_count > 0:
        arr[i] = 1
        once_count -= 1
        i += 1
    while two_count > 0:
        arr[i] = 2
        two_count -= 1
        i += 1

    print([i for i in arr])


move_zeros_once_two([0, 1, 1, 0, 1, 2,
                     1, 2, 0, 0, 0, 1])
