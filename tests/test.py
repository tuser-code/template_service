import os
import sys
import asyncio
import grpc
import unittest
from loguru import logger

sys.path.append(os.getcwd())

import api.grpc.t_service_pb2 as t_service_pb2
import api.grpc.t_service_pb2_grpc as t_service_pb2_grpc


class GRPCClient():
    """grpc client for robo server"""

    def __init__(self, server_address_port):
        self.server_address_port = server_address_port
        self.options = (('grpc.enable_http_proxy', 0),)

    async def get_doc(self, doc_name:str, **params)->str:
      logger.info('')
      try:
          async with grpc.aio.insecure_channel(self.server_address_port, options=self.options) as channel:
              stub = t_service_pb2_grpc.t_srvStub(channel)
              arg = t_service_pb2.get_doc_request()
              arg.document_name = doc_name
              arg.params.update(params)
              response = await stub.get_doc(arg)
              return response.document
      except grpc.RpcError as rpc_error:
          logger.error(rpc_error)
          return str(rpc_error)




class TestGRPCClient(unittest.IsolatedAsyncioTestCase):
  """ """

  def setUp(self):
    """ """
    self.grpc_client = GRPCClient('localhost:50055')

  async def test_get_doc_by_rpc_client_returned_type(self):
    res = await self.grpc_client.get_doc('template_1.kv', val1=57, 
      val2='sting value')
    self.assertIs(type(res), str)

  async def test_get_doc_by_rpc_client_is_error(self):
    res = await self.grpc_client.get_doc('template_1.kv', 
      quality_staff='Enes Çavdar', val1=57, val2='text info', 
      data=[
      {'proc_id':'1', 'proc_name':'tres', 'control_methods':'control_method'},
      {'proc_id':'2', 'proc_name':'tres', 'control_methods':'control_method'},
      {'proc_id':'3', 'proc_name':'tres', 'control_methods':'control_method'},
      ])
    self.assertFalse('Error' in res)
    print(res)


if __name__ == '__main__':
    unittest.main()