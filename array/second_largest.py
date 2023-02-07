def second_largest(arr: list):
    arr.sort()
    return arr[len(arr) - 2]


print(second_largest([1, 2, 3, 4, 5]))
