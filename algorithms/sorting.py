# 1) Insertion Sort
# 2) Heap Sort
# 3) Selection Sort
# 4) Merge Sort
# 5) Quick Sort
# 6) Counting Sort

# ------------------------------------------------------------------------------
# SELECTION SORT
#     64, 25, 12, 22, 11

# For the first position in the sorted array,
# the whole array is traversed from index 0 to 4
# sequentially. The first position where 64 is stored
# presently after traversing whole array it is clear
# that 11 is the lowest value.
#
# This replaces 64 with 11. after first iteration 11 which happens to be
# the least value in the array tends to appear in the first position

# 11, 25, 12, 22, 64
#
# for the second position where 25 is present again traverse the rest of the
# array .

# 11, 12, 25, 22, 64
#
# goes on


# -----------------------------------------------------------------------------

# # BUBBLE SORT ALGORITHM
#     Bubble sort is the simplest sorting algorithm that works by
#     repeatedly swapping the adjacent elements if they are in the
#     wrong order.

# 5, 1, 4, 2 ,8


# # first pass
#     5, 1, 4, 2, 8 ---> 1, 5, 4, 2, 8
#     1, 5, 4, 2, 8 ---> 1, 4, 5, 2, 8
#     1, 4, 5, 2, 8 ---> 1, 4, 2, 5, 8
#     1, 4, 2, 5, 8 ---> 1


# ------------------------------------------------------------------------

# Insertion sort
#      similar to way we sort playing cards in our hands. The array is
#      virtually split into a sorted and an unsorted part.value from the
#      unsorted part are picked and placed at the correct position in the
#      sorted array


# 12, 11,  13,  5, 6

# filling the sorted sub array from the unsorted parent array
