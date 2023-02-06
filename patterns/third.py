def reverse_triangle(n: int):
    space = n - 1
    star = 1
    for i in range(1, n+1):
        for j in range(1, space+1):
            print(" ", end="\t")
        for j in range(1, star + 1):
            print("*", end="\t")
        print(" ", end="\n")
        star += 1
        space -= 1


reverse_triangle(5)

# output
#                                 *
#                         *       *
#                 *       *       *
#         *       *       *       *
# *       *       *       *       *
