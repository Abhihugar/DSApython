def triangle_pattern(data: int):
    for i in range(1, data + 1):
        for j in range(1, i + 1):
            print("*", end="\t")
        print(end="\n")


triangle_pattern(5)

# output
# *
# *       *
# *       *       *
# *       *       *       *
# *       *       *       *       *
