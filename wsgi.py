
from flask_cors import *
from flask import Flask

import sys,os
#将项目根目录加入到运行环境
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app_logging import logger
from app.bert_qa import bert_qa as bert_qa_blueprint
# from app.special_regresstion import special_regresstion as special_regresstion_blueprint
# from app.general_corr import general_corr as general_corr_blueprint
# from app.general_regresstion import general_regresstion as general_regresstion_blueprint
# from app.general_arima import general_arima as general_arima_blueprint
# from app.special_population_forecast import special_population as special_population_blueprint
app = Flask(__name__, static_url_path='')
# load config from config.py
app.config.from_pyfile('config.py')
url_prefix=app.config.get('url_prefix', '/api/cisdi/ml/economic')


CORS(app, supports_credentials=True)
# CORS(app, resources=r'/*')


@app.route('/')
def index():
    return "APIs Server"
app.register_blueprint(bert_qa_blueprint, url_prefix=url_prefix)
# app.register_blueprint(general_arima_blueprint, url_prefix=url_prefix)
# app.register_blueprint(general_corr_blueprint, url_prefix=url_prefix)
# app.register_blueprint(general_regresstion_blueprint, url_prefix=url_prefix)
# app.register_blueprint(special_regresstion_blueprint, url_prefix=url_prefix)
# app.register_blueprint(special_population_blueprint,url_prefix=url_prefix)
if __name__ == '__main__':
    host = app.config.get('APP_HOST', 'localhost')
    port = app.config.get('APP_PORT', '28095')
    logger.info('host:{},port:{}'.format(host,port))

    # from werkzeug.contrib.fixers import ProxyFix
    # app.wsgi_app = ProxyFix(app.wsgi_app)

    # app.run(host=host, port=port, threaded=True, debug=True)
    app.run(host=host, debug=False, port=port)
