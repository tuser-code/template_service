import asyncio
from jinja2 import Environment, FileSystemLoader, select_autoescape

from api.grpc.grpc_server import TemplateServicer
from processor import Processor

env = Environment(
    loader = FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

processor = Processor(env)

srv = TemplateServicer('localhost', '50055', processor)

if __name__ == '__main__':
	try:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(srv.serve())
		loop.close()
	except KeyboardInterrupt:
		logger.info('Exiting from App')

