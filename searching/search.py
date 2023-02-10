def binary_search(arr: list, data: int, low: int, high: int):
    if low > high:
        return -1
    mid = (low + high) // 2

    if data == arr[mid]:
        return arr[mid], mid

    elif arr[mid] > data:
        return binary_search(arr, data, low, mid - 1)
    else:
        return binary_search(arr, data, mid + 1, high)


x = [1, 2, 3, 4, 5]
print(binary_search(x, 4, 0, len(x) - 1))
