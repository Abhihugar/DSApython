def tables(n: int):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end="")
            print(" ", end="\n")
        print("", end="\n")


tables(10)