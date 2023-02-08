def count_ones(arr: list):
    # binary search
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < 1:
            high = mid - 1
        elif arr[mid] > 1:
            low = mid + 1
        else:
            if mid == len(arr) or arr[mid + 1] != 1:
                return mid + 1
            else:
                low = mid + 1
    return 0


print(count_ones([1, 1, 1, 0, 0, 0, 0]))