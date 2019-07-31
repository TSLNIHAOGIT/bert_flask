import sys,os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import wsgi as myapp
from waitress import serve
serve(myapp.app, port=28095, url_scheme='https')
