def reverse_pattern(n: int):
    start = n
    space = 0
    for i in range(1, n+1):
        for j in range(1, space+1):
            print("", end="\t")
        for j in range(1, start+1):
            print("*", end="\t")
        print(end="\n")
        space += 1
        start -= 1


reverse_pattern(5)

# output
#
# *	*	*	*	*
# 	*	*	*	*
# 		*	*	*
# 			*	*
# 				*
