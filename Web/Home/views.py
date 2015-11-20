from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home.route('/')
def root():
    return '<h1>Hello World</h1>'


@home.errorhandler(404)
def error_not_found():
    return '<h1>404 Not Found</h1>'