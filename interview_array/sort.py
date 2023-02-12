def sort_arr(arr: list):

    for i in range(len(arr)):
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_element]:
                min_element = j
        arr[i], arr[min_element] = arr[min_element], arr[i]
    print([i for i in arr])


sort_arr([7, 0, 2])
