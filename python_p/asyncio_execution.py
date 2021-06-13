import asyncio
import multiprocessing
import time
from aiter_class import Aiter


async def sum_list(number):
    ans = 0
    async for i in Aiter(range(number)):
        ans += i
    print(ans)
    return ans


async def range_sum(number):
    print(f'started for {number}')
    a = await sum_list(number)
    print(f'Sum calculated for {number}: {a}')


async def main(numbers, loop):
    tasks = []

    for number in numbers:
        task = loop.create_task(range_sum(number))
        # task = asyncio.ensure_future(range_sum(number))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    numbers = [100000 + x for x in range(5)]
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(numbers, loop))
    # asyncio.get_event_loop().run_until_complete(main(numbers))
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
