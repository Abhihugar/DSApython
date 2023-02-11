def bubble_sort_arr(arr: list):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print([i for i in arr])


bubble_sort_arr([5, 1, 4, 2, 8])
