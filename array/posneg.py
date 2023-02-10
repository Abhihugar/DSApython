# input [-1, 2, -3, 4, 5, 6, -7, 8, 9]

def pos_neg_seg(arr: list):
    i = -1

    for j in range(len(arr)):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    for i in arr:
        print(i, end="\n")


pos_neg_seg([-1, 2, -3, 4, 5, 6, -7, 8, 9])
