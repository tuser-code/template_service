from loguru import logger
from google.protobuf import json_format

class Processor():

	def __init__(self, templating_engine):
		logger.trace('')
		self.t_engine = templating_engine

	async def get_doc(self, doc_name:str, params:dict)->str:
		logger.info('')
		params = json_format.MessageToDict(params)
		template = self.t_engine.get_template(doc_name)
		return template.render(**params)