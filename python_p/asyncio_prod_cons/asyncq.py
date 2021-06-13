import asyncio
import itertools as it
import os
import random
import time


async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(a: int = 1, b: int = 5, caller=None):
    i = random.randint(0, 10)
    if caller:
        print(f'{caller} sleeping for {i} seconds')
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):
        await randsleep(caller=f'Producer {name}')
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f'Producer {name} added <{i}> to queue.')


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f'Consume {name}')
        i, t = await q.get()
        now = time.perf_counter()
        print(f'Consumer {name} got element <{i}>'
              f' in {now-t:0.5} seconds.')
        q.task_done()


async def main(loop, nprod: int, ncon: int, ):
    q = asyncio.Queue()
    producers = [loop.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [loop.create_task(consume(n, q)) for n in range(ncon)]
    # loop.run_until_complete(*producers)
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()


if __name__ == '__main__':
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--nprod', type=int, default=5)
    parser.add_argument('-c', '--ncon', type=int, default=10)
    ns = parser.parse_args()
    print(ns)
    loop = asyncio.get_event_loop()
    start = time.perf_counter()
    asyncio.get_event_loop().run_until_complete(main(loop, **ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f'Program completed in {elapsed:0.5f} seconds.')
