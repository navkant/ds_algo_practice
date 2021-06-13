import multiprocessing
import time


def range_sum(number):
    ans = sum([i for i in range(number)])
    print(f'Calculated sum for {number}')
    return ans


def list_sum(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(range_sum, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    list_sum(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
