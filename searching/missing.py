def find_missing_number(arr: list):
    n = len(arr)
    total_sum = (n+1)*(n + 2)//2
    sum_arr = 0
    for i in range(len(arr)):
        sum_arr += arr[i]
    return total_sum - sum_arr


print(find_missing_number([1, 2, 3, 5]))