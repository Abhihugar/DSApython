def occurence_count(arr: list):
    obj = dict()
    for i in range(len(arr)):
        if arr[i] in obj:
            obj[arr[i]] += 1
        else:
            obj[arr[i]] = 1
    return obj


print(occurence_count([1, 2, 2, 2, 2, 3, 4, 7, 8, 8]))
