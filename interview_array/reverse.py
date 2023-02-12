def reverse_arr(arr: list):
    start = 0
    end = len(arr) - 1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    print([i for i in arr])


reverse_arr([4, 5, 1, 2])


def reverse_arr(arr: list):

    for i in range(len(arr)-1, -1, -1):
        print(arr[i])


reverse_arr([4, 5, 1, 2])