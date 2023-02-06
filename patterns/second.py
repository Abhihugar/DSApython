def reverse_tri_angle(n: int):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print(end="\n")


reverse_tri_angle(5)


# output
#
# *       *       *       *       *
# *       *       *       *
# *       *       *
# *       *
# *
