Web Module
==========
The Web Module is built using Flask blueprints. You'll find the structure is functional. The API is in API and the regular website is in Home.
Each one is assigned to a blueprint and the module is loaded as a single app in __init__ which is then pulled in by viaduct's main module.

For information on the API, please see :doc:`API`.

Website Routes
==============
This will document all current Flask routes.

.. http:get:: /

   Root of the server.

   :statuscode 200: All good.
   :statuscode 302: You should run away, this isn't us.
   :statuscode 404: We're not up for some reason.
   :statuscode 503: Maintenance mode has been turned on.


Adding Routes
=============
This should probably go somewhere else - note to self.

Adding new routes follows the standard flask procedure. Go to API or Home, open views and add routes to the blueprints. As the blueprints are automatically combined and loaded for you, nothing else is required.
You can make your own blueprints by creating a new folder and a new views.py. Make sure you then add your blueprint to __init__.py and register that blueprint with the app so viaduct can import it.