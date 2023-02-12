def sub_arr_sum(arr: list, sum_sub: int):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if sum_sub == sum(arr[i:j]):
                print(arr[i:j])
                break


sub_arr_sum([15, 2, 4, 8, 9, 5, 10, 23], 23)