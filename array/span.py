def span_of_arr(arr: list):
    max_arr = arr[0]
    min_arr = arr[0]
    for i in arr:
        if i > max_arr:
            max_arr = i
        if i < min_arr:
            min_arr = i

    span = max_arr - min_arr
    return {
        "span": span,
        "max": max_arr,
        "min": min_arr
    }


print(span_of_arr([1, 2, 3, 4, 5]))
