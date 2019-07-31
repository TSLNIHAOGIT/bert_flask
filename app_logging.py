# -*- coding:utf8 -*-
import logging
from logging.handlers import RotatingFileHandler
import os
logging.basicConfig(format='[%(asctime)s.%(msecs)03d][%(process)d][%(levelname)s][%(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('Macroeconomic model')
logger.setLevel(logging.DEBUG)
#绝对路径
path=os.path.abspath(os.path.join(os.path.dirname(__file__),'log/macroeconomic_model.log'))

""" 输出日志到日志文件 """
rotatingFileHandler = RotatingFileHandler(path, maxBytes=500000, backupCount=2,encoding='utf8')
rotatingFileHandler.setFormatter(logging.Formatter(fmt='{%(asctime)s.%(msecs)03d} [%(thread)d] %(levelname)s - %(message)s',
                                                   datefmt='%Y-%m-%d %H:%M:%S'))
# 设置级别如果低于设置的级别则无效
rotatingFileHandler.setLevel(logging.INFO)
logger.addHandler(rotatingFileHandler)
