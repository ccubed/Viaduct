from flask import Flask
from .API.views import api
from .Home.views import home

app = Flask(__name__)

# This registers the API. I assume you don't have a subdomain.
# If you have a subdomain, change url_prefix to subdomain and change /api to your fully qualified subdomain.
# Ex: subdomain='api.foo.com'
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(home)
