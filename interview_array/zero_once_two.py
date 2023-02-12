def sort_zero_once_two(arr: list):
    count_zero = 0
    count_one = 0
    count_two = 0
    for i in range(len(arr)):
        match arr[i]:
            case 0:
                count_zero += 1
            case 1:
                count_one += 1
            case 2:
                count_two += 1
    j = 0
    while count_zero > 0:
        arr[j] = 0
        count_zero -= 1
        j += 1
    while count_one > 0:
        arr[j] = 1
        count_one -= 1
        j += 1
    while count_two > 0:
        arr[j] = 2
        count_two -= 1
        j += 1
    print([i for i in arr])


sort_zero_once_two([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])