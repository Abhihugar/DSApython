import asyncio


async def sum_of_digits(data: int):
    """
    sum of total digits
    :param data:
    :return: total sum
    """
    total_sum = 0
    for i in range(data):
        total_sum += i
    print(total_sum)


async def main():
    await sum_of_digits(100)

asyncio.run(main())
