def seg_even_odd(arr: list):
    output = list()
    for i in arr:
        print(i)
        if i % 2 == 0:
            print(i, end="\n")
            if i not in output:
                output.append(i)
                arr.remove(i)
    # print(arr)
    return output + arr


print(seg_even_odd([1, 3, 2, 4, 7, 6, 9, 10]))
