# Web Server

import Backend, simplejson as json
from gevent import pywsgi

class Webserver:
    
    def __init__(self, x):
        self.stoneref = x
                
    def responseHandler(self, env, start_response):
        if env['PATH_INFO'].contains('api'):
            response = self.apiRouter(env['PATH_INFO'])
        else:
            response = self.httpRouter(env['PATH_INFO'])
        if response == '404':
            start_response('404 Not Found',[('Content-Type','text/html')])
            return [b'<h1>Not Found</h1>']
        else:
            start_response('200 Ok',[('Content-Type','text/html')])
            return response
            
    def apiRouter(self, path):
        parts = path.split('/')
        if parts[2] == 'pair':
            temp = self.stoneref.getpair(parts[3],8)
            if temp == 'Error':
                return json.dumps({'Result': 'Error', 'Details': 'There are only 15 DBs'})
            else:
                return json.dumps({'Result': 'Success', 'Value': temp})
        else:
            return '404'
                
    def httpRouter(self, path):
        if path == '/':
            return [b'<h1>Hello World</h1>']
        else:
            return '404'