def insertion_sort_arr(arr: list):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            else:
                break

    print([i for i in arr])


insertion_sort_arr([12, 31, 25, 8, 32, 17])
