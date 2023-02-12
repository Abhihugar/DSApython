def span_arr(arr: list):
    max_element = arr[0]
    min_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
        if arr[i] < min_element:
            min_element = arr[i]
    return {
        "max_element": max_element,
        "min_element": min_element,
        "span": max_element - min_element
    }


print(span_arr([3, 2, 1, 56, 10000, 167]))