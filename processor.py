from loguru import logger
from jinja2 import Environment


def debug(text):
    print(text)
    print('------------------------')
    return ''


class Processor():

    def __init__(self, environment: Environment):
        logger.trace('')
        self.environment = environment
        self.environment.filters['debug'] = debug

    async def get_doc(self, doc_name: str, params: dict) -> str:
        logger.info('')
        try:
            template = self.environment.get_template(f'{doc_name}/{doc_name}')
            res = template.render(params=params)#.replace('\n', '\\n')
            with open('tmp.kv', 'w') as file:
                file.write(res)
        except Exception as e:
            logger.error(type(e))
            logger.error(e)
            res = ''
        return res
