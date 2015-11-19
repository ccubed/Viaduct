# HTML Routes
@app.route('/')
def root():
    return '<h1>Hello World!</h1>'


@app.errorhandler(404)
def page_not_found(error):
    return '<h1>404 Not Found</h1>', 404


