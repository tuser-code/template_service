from loguru import logger
import asyncio
import grpc
import api.grpc.t_service_pb2 as t_service_pb2
import api.grpc.t_service_pb2_grpc as t_service_pb2_grpc


port = '50051'


class TemplateServicer(t_service_pb2_grpc.t_srvServicer):
    '''Doc string'''

    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def serve(self):
        logger.info('')
        server = grpc.aio.server()
        t_service_pb2_grpc.add_t_srvServicer_to_server(self, server)
        listen_addr = f'{self.host}:{self.port}'
        listen_addr = server.add_insecure_port(listen_addr)
        logger.info(f"Starting server on {listen_addr}")
        await server.start()
        await self.im_alive()
        await server.wait_for_termination()

    async def im_alive(self):
        while True:
            await asyncio.sleep(1)
            print('---')