from flask import  request, jsonify
import time
import sys,os
#将项目根目录加入到运行环境
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
##route使用
from app.bert_qa import bert_qa
# from part_code_data.arima import gdp_percent_arima
# from final_code_data.general_model.ARIMA import ARIMA2
# from app.utils import judge_null_text


from app_logging import logger
import pandas as pd
import numpy as np

# app = Flask(__name__)
# CORS(app, supports_credentials=True)
# CORS(app, resources=r'/*')

''''
是一种服务端与客户端的形式；服务端发起服务，客户去访问（以特定的链接加参数才可以）
'''



#服务端获取客户端发来的json数据
@bert_qa.route('/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):

  try:

        logger.info('开始进入模型，服务端获取数据')
        t1=time.time()
        content = request.get_json(silent=True,force=True)
        logger.info('from client content:{}'.format(content)) # Do your processing
        #response must be a string\tupe\ and so on.
        logger.info('将获取的json数据转为dataframe数据框')
        # python客户端传来的字符创，网络客户端传来的是dict
        logger.info('type content{}'.format(type(content)))
        # if isinstance(content,str):
        #   df_new = pd.read_json(content)
        #   logger.info('data:{}'.format(df_new.head()))
        #   logger.info('调用gdp_percent_arima.read_data_new函数')
        #
        #   # data_train,data_test,row_number=gdp_percent_arima.read_data_new(df_new)
        #   predict_periods=3
        # elif isinstance(content,dict):
        #   # df_new = pd.DataFrame(content)
        #   #将json数据格式转为模型的输入格式
        #   logger.info('将客户端传过来的json数据转为算法输入的格式')
        #   column_name = content['param'][0][0]['historyData'][0]
        #   logger.info('column_name:{}'.format(column_name))
        #   data = content['param'][0][0]['historyData'][1:]
        #   # logger.info('ori_data:{}'.format(np.array(data).shape))
        #
        #   data_train = pd.DataFrame(data=data, columns=column_name)
        #   logger.info('data_train_shape:{}'.format(data_train))
        #   # 判断数据是否含有空值和文本内容
        #   train_res_str_null = judge_null_text.judge_null_str_value(data_train)
        #   data_train = train_res_str_null['df']
        #
        #
        #
        #   # name_list = data_train.drop(labels=['date'], axis=1).columns
        #
        #   logger.info('data_train{}'.format(data_train.head()))
        #
        #   test_ori_data = content['param'][1][0]['predictData']
        #   if test_ori_data != '':
        #     test_name = content['param'][1][0]['predictData'][0]
        #     test_data = content['param'][1][0]['predictData'][1:]
        #     data_test = pd.DataFrame(data=test_data, columns=test_name)
        #
        #     # 判断数据是否含有空值和文本内容
        #
        #     test_res_str_null = judge_null_text.judge_null_str_value(data_test)
        #
        #     data_test = test_res_str_null['df']
        #
        #     #要把训练和测试数据都获取之后再判断是否存在空值，否则训练数据存在空值，那么
        #     #就不会获取测试数据，那么后面就会显示测试数据变量为定义
        #     if len(train_res_str_null) > 2:
        #       raise Exception('存在空值')
        #
        #     if len(test_res_str_null) > 2:
        #       raise Exception('存在空值')
        #
        #     logger.info('data_test{}'.format(data_test.head()))
        #     test = ARIMA2.read_data_new(data_test)
        #
        #     # for each_name in test_name:
        #     #     data_test_each = data_test[each_name]
        #     # logger.info('data_test_each {}'.format(data_test_each.head()))
        #   else:
        #     test=False
        #
        #   #本地to_list和tolist都可以用，但是服务器端不可以使用to_list
        #   logger.info('column_name[0]{}'.format(column_name[0]))
        #   last_time = data_train[column_name[0]].tolist()[-1]
        #   logger.info('last_time：{}'.format(last_time))
        #
        #   predict_periods = content['param'][2][0]['predict_periods']
        #   time_periods_list=range(int(last_time)+1,int(last_time)+int(predict_periods)+1)
        #   if predict_periods!='':
        #     try :
        #       predict_periods=int(predict_periods)
        #     except Exception as e:
        #       logger.info('期数转为整型错误{}'.format(e))
        #       predict_periods = 3
        #   else:
        #     logger.info('预测期数未传默认为3期数')
        #     predict_periods = 3
        #
        # else:
        #   logger.info('传入参数类型错误')
        #
        #
        #
        # # data_train = data_train['美国']
        # # data_test = data_test['美国']
        # # name_list=['美国','中国','日本','德国','英国']
        #
        # all_country_results=[]
        # all_country_best_params=[]
        # all_relative_error_mean=[]
        #
        # logger.info('读取训练数据')
        # data = ARIMA2.read_data_new(data_train)
        #
        #
        #
        # t2 = time.time()
        # # 根据参数的顺序来进行选择不同的执行
        # for data_order in range(1, len(data)):
        #   data_subset = data[data_order]
        #   if test is not False:
        #     test_data_subset = test[data_order]
        #     # print('test_data_subset',type(test_data_subset),test_data_subset)
        #   else:
        #     test_data_subset = False
        #
        #   # print('dd', data_order, data_subset, '\n\n')
        #   logger.info('调用ARIMA2模型;{}'.format(data_order))
        #
        #   results = ARIMA2.auto_arima_para_new(data_subset, predict_periods=predict_periods,
        #                                   data_test_subset=test_data_subset)
        #   if results is None:
        #     logger.info('This problem is unconstrained，无法分析')
        #   else:
        #     # print('output_result', results)
        #     all_country_results.append(results['predict_value'])
        #     all_country_best_params.append(results['best_params'])
        #
        #     if test is not False:
        #         all_relative_error_mean.append(results['relative_error_mean'])
        #     else:
        #         all_relative_error_mean=[''  for each in range(len(data)-1)]
        #
        #
        # logger.info('all_country_results:{}'.format(all_country_results))
        # # results.headers['Access-Control-Allow-Origin'] = '*'
        # results['success']='0'
        # logger.info('len(time_periods_list){}'.format(len(time_periods_list)))
        # logger.info('shape{}'.format(np.array(all_country_results).T.shape))
        # predict_time_value = np.column_stack((time_periods_list, np.array(all_country_results).T)).tolist()
        #
        # logger.info('len(all_relative_error_mean){}'.format(len(all_relative_error_mean)))
        # logger.info('all_country_best_params shape{}'.format(np.array(all_country_best_params).shape))
        #
        # all_error_params = np.column_stack((np.array([column_name[1:],all_relative_error_mean]).T, all_country_best_params)).tolist()
        #
        # logger.info('predict_time_value{}'.format(predict_time_value))
        #
        # # logger.info('predict_time_value{}'.format(predict_time_value))
        # results['predict_value']=predict_time_value
        # results['all_error_params']=all_error_params
        # logger.info('results:{}'.format(results))
        # # print('results',results)
        # t3=time.time()
        # logger.info('数据处理耗时：{}s'.format(t2 - t1))
        # logger.info('模型调用耗时：{}s'.format(t3-t2))
        # logger.info('总耗时{}s'.format(t3-t1))
        #
        #
        # # final_results={}
        # # final_results['ddd']=results
        # # logger.info('final_results:{}'.format(final_results))
        return jsonify(content)
        # return jsonify(content)
  except Exception as e:
         print(e)

         #
         # ####对于数据结果不完整的情况，可以使用try_except_else ,
         # # ##报错时else部分不执行，根据这个觉得返回哪些字段（报错情况下）
         # #判断训练数据是否包含文字内容和缺失值
         # if len(train_res_str_null) > 2:
         #   null_value =  train_res_str_null['null_row_num']
         # else:
         #   null_value = '0'
         #
         # if test_ori_data != '':
         #   test_is_str=test_res_str_null['is_str']
         #   if len(test_res_str_null) > 2:
         #     test_null_value =  test_res_str_null['null_row_num']
         #   else:
         #     test_null_value = '0'
         # else:
         #     #输出0时正常：有测试数据时的正常和没有测试数据的正常
         #     test_null_value = '0'
         #     test_is_str='0'
         #
         #
         # fail_res={'success': '1',
         #           'null_value_rows_num': null_value,'is_str':train_res_str_null['is_str'],
         #           'test_null_value_rows_num':test_null_value,'test_is_str':test_is_str,
         #           'message': '调用模型计算接口失败,请查看具体原因......'}
         # logger.info('fail_res:{}'.format(fail_res))
         # return jsonify(fail_res)
         #
         # #
         # # logger.info('出现异常{}'.format(e))
         # # return jsonify({'success':'1','message':'调用模型计算接口失败,请查看具体原因......'})


