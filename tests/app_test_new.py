#encoding=utf-8
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
data_json={
      "paragraphs": [
        {
          "id": "TRIAL_800",
          "context": "基于《跑跑卡丁车》与《泡泡堂》上所开发的游戏，由韩国Nexon开发与发行。中国大陆由盛大游戏运营，这是Nexon时隔6年再次授予盛大网络其游戏运营权。台湾由游戏橘子运营。玩家以水枪、小枪、锤子或是水炸弹泡封敌人(玩家或NPC)，即为一泡封，将水泡击破为一踢爆。若水泡未在时间内踢爆，则会从水泡中释放或被队友救援(即为一救援)。每次泡封会减少生命数，生命数耗完即算为踢爆。重生者在一定时间内为无敌状态，以踢爆数计分较多者获胜，规则因模式而有差异。以2V2、4V4随机配对的方式，玩家可依胜场数爬牌位(依序为原石、铜牌、银牌、金牌、白金、钻石、大师) ，可选择经典、热血、狙击等模式进行游戏。若游戏中离，则4分钟内不得进行配对(每次中离+4分钟)。开放时间为暑假或寒假期间内不定期开放，8人经典模式随机配对，采计分方式，活动时间内分数越多，终了时可依该名次获得奖励。",
          "qas": [
            {
              "question": "生命数耗完即算为什么？",
              "id": "TRIAL_800_QUERY_0",
              "answers": [
                {
                  "text": "踢爆",
                  "answer_start": 127
                }
              ]
            },
            {
              "question": "若游戏中离，则多少分钟内不得进行配对？",
              "id": "TRIAL_800_QUERY_1",
              "answers": [
                {
                  "text": "4分钟",
                  "answer_start": 301
                }
              ]
            },
            {
              "question": "玩家用什么泡封敌人？",
              "id": "TRIAL_800_QUERY_2",
              "answers": [
                {
                  "text": "玩家以水枪、小枪、锤子或是水炸弹泡封敌人",
                  "answer_start": 85
                }
              ]
            },
            {
              "question": "游戏的模式有哪些？",
              "id": "TRIAL_800_QUERY_3",
              "answers": [
                {
                  "text": "可选择经典、热血、狙击等模式进行游戏。",
                  "answer_start": 275
                }
              ]
            }
          ]
        }
      ],
      "id": "TRIAL_800",
      "title": "泡泡战士"
    }

def post_test(post_server=True,server_name=None):
  if post_server:
    # url='http://apis.cisdi.amiintellect.com/api/cisdi/ml/economic/{}/1234'.format(server_name)
    url = 'http://apis.cisdi.amiintellect.com/api/cisdi/ml/economic/{}/1234'.format(server_name)
  else:
    url = 'http://8113.204.147.34:8888/api/cisdi/ml/economic/{}/1234'.format(server_name)  # 28095
  # data_json=switch_post[server_name]

  res = requests.post(url,# json={"mytext":"from client :lalala"}
                      json=data_json
                      )
  print(res)
  if res.ok:
      # print('res.json()',res)
      logger.info('from server response:{}'.format(res.json()))#response是post请求的返回值

if __name__=='__main__':
  post_test(post_server=False, server_name='add_message')
