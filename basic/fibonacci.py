def fibonacci_series(data: int):
    """
    print the fibonacci series
    upto given number.
    :param data:
    :return:
    """
    a = 0
    b = 1
    for i in range(data):
        c = a + b
        a = b
        b = c
        print(a)


fibonacci_series(10)
