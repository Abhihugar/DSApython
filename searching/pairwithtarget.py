def pair_add(arr: list, target):
    obj = dict()

    for i in range(len(arr)):
        if target - arr[i] in obj:
            print(obj)
            return arr[i], obj.get(target-arr[i])
        else:
            obj[arr[i]] = arr[i]

    return -1


print(pair_add([1, 8, 30, 40, 100], 150))
