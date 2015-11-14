# -*- coding: utf-8 -*-

from gevent import pywsgi

from Web import app

if __name__ != '__main__':
    print("Sorry, can't be run as a submodule.")
else:
    webserver = pywsgi.WSGIServer(('localhost', 8443), app)
    webserver.serve_forever()
