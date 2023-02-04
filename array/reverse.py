def reverse(arr: list):
    low = 0
    high = len(arr) - 1
    while low <= high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low += 1
        high -= 1

    for i in arr:
        print(i, end=" ")


data = ([1, 2, 3, 4, 5])
reverse(data)
