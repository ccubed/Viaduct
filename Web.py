# Web Server

import Backend, simplejson as json
from gevent import pywsgi

class Webserver:
    
    def __init__(self, x):
        self.stoneref = x
                
    def responsehandler(self, env, start_response):
        if 'api' in env['PATH_INFO']:
            response = self.apirouter(env['PATH_INFO'])
        else:
            response = self.httprouter(env['PATH_INFO'])
        if response == '404':
            start_response('404 Not Found',[('Content-Type','text/html')])
            return [b'<h1>Not Found</h1>']
        else:
            if 'api' in env['PATH_INFO']:
                start_response('200 Ok', [('Content-Type', 'text/json')])
                return [str.encode(response)]
            else:
                start_response('200 Ok', [('Content-Type', 'text/html')])
                return response
            
    def apirouter(self, path):
        parts = path.split('/')
        if parts[2] == 'pair':
            temp = self.stoneref.getpair(parts[3], 8)
            if 'Error' in temp:
                return json.dumps({'Result': 'Error', 'Details': temp.split('-')[1].strip()})
            else:
                return json.dumps({'Result': 'Success', 'Details': temp})
        else:
            return '404'
                
    def httprouter(self, path):
        if path == '/':
            return [b'<h1>Hello World</h1>']
        else:
            return '404'
