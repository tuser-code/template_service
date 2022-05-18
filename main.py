import asyncio
from jinja2 import Environment, FileSystemLoader, select_autoescape
from loguru import logger
from api.grpc.grpc_server import TemplateServicer
from processor import Processor
import config as CONFIG


environment = Environment(
    loader = FileSystemLoader(['templates', 'templates_kv']),
    autoescape=select_autoescape()
)

processor = Processor(environment)

srv = TemplateServicer(CONFIG.SERVER, CONFIG.PORT, processor)

if __name__ == '__main__':
	try:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(srv.serve())
		loop.close()
	except KeyboardInterrupt:
		logger.info('Exiting from App')

