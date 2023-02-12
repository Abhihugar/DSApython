def kth_smallest(arr: list, k: int):
    arr.sort()
    return arr[k-1]


print(kth_smallest([7, 10, 4, 3, 20, 15], 3))