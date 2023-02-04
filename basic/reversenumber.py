def reverse_number(data: int):
    """
    reverse the given integer
    excluding initial zero.
    :param data: input data
    :return: reverse number
    """
    rev = 0
    while data > 0:
        reminder = data % 10
        data = data // 10
        rev = rev * 10 + reminder
    return rev


print(reverse_number(120))