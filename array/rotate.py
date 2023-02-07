def rotate_arr(arr: list, k: int):
    def reverse_arr(data: list, low: int, high: int):
        while low <= high:
            temp = data[low]
            data[low] = data[high]
            data[high] = temp
            low += 1
            high -= 1

    reverse_arr(arr, 0, k - 1)
    reverse_arr(arr, k, len(arr) - 1)
    reverse_arr(arr, 0, len(arr) - 1)

    return [i for i in arr]


print(rotate_arr([1, 3, 5, 7, 9], 2))