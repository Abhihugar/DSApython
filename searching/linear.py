def linear_search(arr: list, target: int):
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break
    return index


print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 110))
