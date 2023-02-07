def distinct_arr(arr: list):
    output = []
    for i in arr:
        if i not in output:
            output.append(i)
    return output


print(distinct_arr([12, 10, 9, 45, 2, 10, 10, 45]))
