def any_base_decimal(data: int, base: int):
    """
    convert any base to decimal number
    system.
    :param data: input data
    :param base: conversion base
    :return: output.
    """
    power = 1
    output = 0
    while data > 0:
        reminder = data % base
        output += reminder * power
        data = data // base
        power *= 8
    return output


print(any_base_decimal(1266, 10))
