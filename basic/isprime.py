def is_prime(data: int):
    count = 0
    for i in range(2, data):
        if data % i == 0:
            count += 1
            break

    if count == 0:
        print(count)
        print("it is prime number")
    else:
        print("it is not prime number")


is_prime(10)
