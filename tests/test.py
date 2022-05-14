import os
import sys
import asyncio
import grpc
import unittest
from loguru import logger

sys.path.append(os.getcwd())

from api.grpc.grpc_client import GRPCClient


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


if __name__ == '__main__':
    unittest.main()