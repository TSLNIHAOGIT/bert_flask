import sys
import os
# print(os.path)
# print(dirname(__file__))
# print(abspath(dirname(__file__)))
#定义搜索路径的优先顺序，序号从0开始，表示最大优先级，sys.path.insert()加入的也是临时搜索路径，程序退出后失效。
# sys.path.insert(0, abspath(dirname(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

# print('nn path',os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

#__file__主要是解决导入某个模块时，该模块又导入了其他模块这样由于路径导入错误而报错
# print (os.path.abspath(os.path.dirname(__file__)))

from app_logging import logger
logger.info('hello32')
logger.info('哈喽32')
