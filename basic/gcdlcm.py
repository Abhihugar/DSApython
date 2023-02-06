def find_gcd_lcm(n1: int, n2: int):
    """
    find the gcd and lcm of
    the two given numbers.
    :param n1: small number
    :param n2: larger number
    :return: gcd and lcm
    """
    l1 = n1
    l2 = n2

    while l2 % l1 != 0:
        reminder = l2 % l1
        l2 = l1
        l1 = reminder

    gcd = l1

    lcm = int(n1 * n2) // gcd
    return {
        "gcd": gcd,
        "lcm": lcm
    }


print(find_gcd_lcm(24, 36))
