from flask import *

from Backend import *

app = Flask(__name__)


@app.route('/')
def root():
    return '<h1>Hello World!</h1>'


@app.route('/api/pair/<key>')
def api_getkey(key):
    temp = getpair(key, 8)
    if 'Error' in temp:
        return json.dumps({'Result': 'Error', 'Details': temp.split('-')[1].strip()})
    else:
        return json.dumps({'Result': 'Success', 'Details': temp})


@app.errorhandler(404)
def page_not_found(error):
    return '<h1>404 Not Found</h1>', 404
