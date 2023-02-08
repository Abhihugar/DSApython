def first_repeating_element(arr: list):
    min_index = -1
    obj = dict()
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in obj.keys():
            min_index = i
        else:
            obj[arr[i]] = 1
    if min_index > 0:
        return {
            "first_repeating_index": min_index,
            "arr": arr[min_index]
        }
    return min_index


print(first_repeating_element([10, 5, 3, 4, 3, 5, 6]))
