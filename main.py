import asyncio


async def main():
	await asyncio.sleep(2)
	print('----')

if __name__ == '__main__':
	try:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main())
		loop.close()
	except KeyboardInterrupt:
		logger.info('Exiting from App')
