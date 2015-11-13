# -*- coding: utf-8 -*-

from Backend import *
from Web import *
from gevent import pywsgi

if __name__ != '__main__':
    print("Sorry, can't be run as a submodule.")
else:
    Rc = Stonework()
    WebTest = Webserver(Rc)
    Server = pywsgi.WSGIServer(('localhost', 8443), WebTest.responsehandler)
    Server.serve_forever()
