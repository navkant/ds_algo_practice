import time


def range_sum(number):
    return sum([i for i in range(number)])


def list_sum(numbers):
    for number in numbers:
        range_sum(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    list_sum(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
