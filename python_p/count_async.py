import time
import asyncio


async def count(secs):
    print(f'started function call with {secs}s')
    print('one')
    await asyncio.sleep(1)
    print(f'completed function call with {secs}s')
    print('two')


async def main():
    await asyncio.gather(count(2), count(50), count(10))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.get_event_loop().run_until_complete(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
