def find_peak(arr: list):
    max_element = 0
    for i in range(len(arr)):
        if arr[i] > max_element:
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                max_element = arr[i]
    return max_element


print(find_peak([5, 10, 20, 15]))
