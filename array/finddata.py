def find_element(arr: list, data: int):
    """
    This method returns the and find the
    index of data in given array.
    :param arr: array
    :param data: element
    :return: index
    """
    index = -1
    for i in range(len(arr)):
        if data == arr[i]:
            index = i
            return index
    return index


print(find_element([1, 2, 3, 4, 5], 10))
