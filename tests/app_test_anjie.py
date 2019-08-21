import requests
import os,sys
import numpy as np
import json
import time
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

def post_processing(post_server=True,server_name=None,port=None,data=None):
    if post_server:
        ###安捷地址将服务器ip+端口（8888）映射成一个了，
        url='http://jupyter.test.anjie.superlucy.net:8080/api/ml/bertQA/{}'.format(server_name)
        #url='http://apis.customs.dev4.amiintellect.com/api/ml/bertQA/{}'.format(server_name)
    else:
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