"""
This program converts decimal to
given base.
"""


def decimal_to_any_base(data: int, base: int):
    """

    :param data: given input
    :param base: conversion base
    :return:  number
    """
    power = 1
    output = 0
    while data > 0:
        reminder = data % base
        output += reminder * power
        data = data // base
        power *= 10
    return output


print(decimal_to_any_base(694, 8))
