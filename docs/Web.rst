Web Module
==========
The Web Module is built using Flask. As such it is easy to define routes for the API, code in responses and utilize elements of werkzeug and jinja2.
The Web Module is responsible for both a website made possible using the template syntax of jinja2 and the easy routing of flask and for an api that returns data to clients that choose to interact with the game in that manner.

Website Portion
===============
    ..py:method root
    Returns the document root of the website portion of the web module.

    ..py:method page_not_found
    Handles 404 error

API
===

The API follows normal conventions of RESTful apis and returns all its data in JSON format. You can find details on that below.
The documentation here is only about the python functions in Web.py. For information on the API look at the :doc:`API` documentation.

    ..py:getpair(key)
    Return the value of Key in DB 8 of Redis. This is a testing function.

Adding New Routes
=================
To add a new route, follow the standard flask process. This is wrapped in gevent so keep that in mind, but really that shouldn't matter much.
To add a new API route, just make the route response to the location of your API and define your functions with the passed parameters.
Since we're using Flask, you have access to all of those constructs.