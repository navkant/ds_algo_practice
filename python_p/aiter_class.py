import asyncio


class Aiter:
    def __init__(self, iterable):
        self.iter_ = iter(iterable)

    async def __aiter__(self):
        return self

    async def __anext__(self):
        await asyncio.sleep(0)
        try:
            object = next(self.iter_)
        except StopIteration:
            raise StopAsyncIteration  # :-) PEP492 - "To stop iteration __anext__ must raise a StopAsyncIteration exception"

        return object
