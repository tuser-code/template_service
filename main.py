import asyncio
from api.grpc.grpc_server import TemplateServicer


srv = TemplateServicer('localhost', '50055')

if __name__ == '__main__':
	try:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(srv.serve())
		loop.close()
	except KeyboardInterrupt:
		logger.info('Exiting from App')
