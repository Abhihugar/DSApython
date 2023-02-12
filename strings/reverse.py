def reverse_word(s: str):
    def reverse_str(s, low: int, high: int):
        while low < high:
            temp = s[low]
            s[low] = s[high]
            s[high] = temp
            low += 1
            high -= 1

    s = list(s)
    start = 0
    while True:
        try:
            end = s.index(" ", start)
            reverse_str(s, start, end - 1)
            start = end + 1
        except ValueError:
            reverse_str(s, start, len(s) - 1)
            break
    s.reverse()
    s = "".join(s)
    print(s)


reverse_word("i love programming very much")
