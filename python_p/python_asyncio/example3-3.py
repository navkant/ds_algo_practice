import asyncio, time

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(3)
    print(f'{time.ctime()} Goodbye!')


def blocking():
	print('Seperate thread started')
	time.sleep(2)
	print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_in_executor(None, blocking)
loop.run_until_complete(task)
pending = asyncio.Task.all_tasks(loop=loop) 
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()