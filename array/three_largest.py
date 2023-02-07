def find_3_largest_element(arr: list):
    first_max = 0
    second_max = 0
    third_max = 0
    for i in arr:
        if i > first_max:
            third_max = second_max
            second_max = first_max
            first_max = i
        elif i > second_max:
            third_max = second_max
            second_max = i

        else:
            third_max = i
    return {
        "first_max": first_max,
        "second_max": second_max,
        "third_max": third_max
    }


print(find_3_largest_element([1, 2, 3, 4, 5]))
