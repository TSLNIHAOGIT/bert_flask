import requests
import os,sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app_logging import logger
import numpy as np


data_json={
    "TRIAL_800_QUERY_0": "\u8e22\u7206",
    "TRIAL_800_QUERY_1": "4\u5206\u949f\u5185\u4e0d\u5f97\u8fdb\u884c\u914d\u5bf9(\u6bcf\u6b21\u4e2d\u79bb+4\u5206\u949f",
    "TRIAL_800_QUERY_2": "\u6c34\u67aa\u3001\u5c0f\u67aa\u3001\u9524\u5b50\u6216\u662f\u6c34\u70b8\u5f39",
    "TRIAL_800_QUERY_3": "\u53ef\u9009\u62e9\u7ecf\u5178\u3001\u70ed\u8840\u3001\u72d9\u51fb\u7b49\u6a21\u5f0f\u8fdb\u884c\u6e38\u620f\u3002"
}

def post_test(post_server=True,server_name=None):
  if post_server:
    url='http://apis.cisdi.amiintellect.com/api/cisdi/ml/economic/{}/1234'.format(server_name)
  else:
    url = 'http://localhost:28095/api/cisdi/ml/economic/{}/1234'.format(server_name)  # 28095
  # data_json=switch_post[server_name]

  res = requests.post(url,# json={"mytext":"from client :lalala"}
                      json=data_json
                      )

  if res.ok:
      # print('res.json()',res)
      logger.info('from server response:{}'.format(res.json()))#response是post请求的返回值

if __name__=='__main__':
  post_test(post_server=False, server_name='add_message')
