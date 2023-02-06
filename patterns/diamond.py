def diamond_pattern(n:int):
    star = 1
    space = n // 2
    for i in range(1, n+1):
        for j in range(1, space + 1):
            print("", end="\t")
        for j in range(1, star + 1):
            print("*", end="\t")
        print(end="\n")

        if i <= n//2:
            space -= 1
            star += 2
        else:
            space += 1
            star -= 2


diamond_pattern(5)


# output
#
# 		*
# 	*	*	*
# *	*	*	*	*
# 	*	*	*
# 		*
