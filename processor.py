from loguru import logger
from google.protobuf import json_format

class Processor():

	def __init__(self, environment):
		logger.trace('')
		self.environment = environment

	async def get_doc(self, doc_name:str, params:dict)->str:
		logger.info('')
		params = json_format.MessageToDict(params)
		template = self.environment.get_template(doc_name + '.kv')
		return template.render(**params)
