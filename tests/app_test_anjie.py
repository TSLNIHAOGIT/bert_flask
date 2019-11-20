#encoding=utf-8
import requests
import os,sys
import numpy as np
import json
import time
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

def post_processing(post_server=True,server_name=None,port=None,data=None):
    if post_server:
        ##服务器上ip和端口绑定
        ###安捷地址将服务器ip+端口（8888）映射成一个了，
        url='http://jupyter.test.anjie.superlucy.net:8080/api/ml/bertQA/{}'.format(server_name)
        #url='http://apis.customs.dev4.amiintellect.com/api/ml/bertQA/{}'.format(server_name)
    else:
        #需要自己加端口
        url = 'http://localhost:{}/api/ml/bertQA/{}'.format(port,server_name)
    res = requests.post(url,json=data)
    if res.ok:
        return res.json()
    else:
        print('NO RESPONSE')

if __name__=='__main__':

    data_json = {'hs_code':'3818001100', 'context':'商品中文名称叫硅片，生产与日本，品牌是SUMCO牌，品牌类型是境外（其他）。本次申报一共有1500片，型号是MS2T1K-25。外观圆形片状，直径12英寸（约300MM），主要成分为单晶硅，掺杂硼元素，硅的纯度99.999999%。硅片是芯片制造的原材料。该硅片是精加工制成，加工工艺包括切片，标识，磨片，清洗，退火，粘片，抛光等，无GTIN，无CAS'}
    t1=time.time()
    #docker 内部测试端口用8889，anjie服务器上端口是8888
    res = post_processing(post_server=True, server_name='prediction',port=8888,data=data_json)
    t2=time.time()
    print('spend time:{}s'.format(t2-t1))
    print(res)
'''
spend time:4.950098514556885s
{'message': 'success', 'code': '0', 'data': [{'answer': '硅片', 'question': 'GTIN'}, {'answer': '99.999999%', 'question': '加工程度'}, {'answer': '切片，标识，磨片，清洗，退火，粘片，抛光等，无GTIN，无CAS', 'question': '出口享惠情况'}, {'answer': '12英寸（约300MM）', 'question': '直径'}, {'answer': '单晶硅，掺杂硼元素，硅的纯度99.999999%。', 'question': '成分'}, {'answer': '圆形片状', 'question': '外观'}, {'answer': '硅片', 'question': '用途'}, {'answer': 'CAS', 'question': 'CAS'}, {'answer': '境外（其他）', 'question': '品牌类型'}]}

spend time:13.27139139175415s
{'data': [{'answer': '生产与日本，品牌是SUMCO牌，品牌类型是境外（其他）。', 'question': '用途'}, {'answer': '无CAS', 'question': 'CAS'}, {'answer': '12英寸', 'question': '直径'}, {'answer': '生产与日本，品牌是SUMCO牌，品牌类型是境外（其他）。', 'question': '出口享惠情况'}, {'answer': '圆形片状', 'question': '外观'}, {'answer': '加工工艺包括切片，标识，磨片，清洗，退火，粘片，抛光等', 'question': '加工程度'}, {'answer': '无GTIN，无CAS', 'question': 'GTIN'}, {'answer': '境外（其他）', 'question': '品牌类型'}, {'answer': '单晶硅', 'question': '成分'}], 'message': 'success', 'code': '0'}
'''