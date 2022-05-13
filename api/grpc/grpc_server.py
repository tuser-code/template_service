from loguru import logger
import asyncio
import grpc
import api.grpc.t_service_pb2 as t_service_pb2
import api.grpc.t_service_pb2_grpc as t_service_pb2_grpc


port = '50051'


class TemplateServicer(t_service_pb2_grpc.t_srvServicer):
    '''Doc string'''

    def __init__(self, host, port, processor):
        self.host = host
        self.port = port
        self.processor = processor

    async def serve(self):
        logger.info('')
        server = grpc.aio.server()
        t_service_pb2_grpc.add_t_srvServicer_to_server(self, server)
        listen_addr = f'{self.host}:{self.port}'
        listen_addr = server.add_insecure_port(listen_addr)
        logger.info(f"Starting server on {listen_addr}")
        await server.start()
        await server.wait_for_termination()

    async def get_doc(self, request, context)->bytes:
        logger.info('')
        ret_data = t_service_pb2.get_doc_response()
        ret_data.document = await self.processor.get_doc(request.document_name, request.params)
        return ret_data