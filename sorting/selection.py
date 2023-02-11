def selection_arr_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print([i for i in arr])


selection_arr_sort([64, 25, 12, 22, 11])


# selecting the first element keeping that element as min and traverse
# whole array by comparing with min value in arr
