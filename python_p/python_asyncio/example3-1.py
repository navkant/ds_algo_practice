# this program is for python 3.5

import asyncio, time

async def main():
	print(f'{time.ctime} Hello!')
	await asyncio.sleep(1)
	print(f'{time.ctime} Goodbye!')


asyncio.run(main())