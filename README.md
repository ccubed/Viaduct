# Viaduct
Viaduct is a Mu server that is meant to bridge the gap between old and new by providing interfaces to the old and new at the same time.

It does this by running the old and new under a single point of entry and using a unified message dispatcher to communicate changes across all the channels.

Viaduct is many things at once and nothing specific at once. It changes the way everything works all at once. It's all of these things:

* A telnet server
* A web server
* Real OOB Communication
* A Restful API
* A new kind of Mu game

# So what's behind all this

Viaduct is using the following libraries to get these things to work together.

* Python 3.5 (https://www.python.org/)
* Greenlet (https://github.com/python-greenlet/greenlet)
* Gevent (http://www.gevent.org)
* Redis (http://redis.io/)
* Redis-py (https://github.com/andymccurdy/redis-py)
* Telnetsrv (https://pypi.python.org/pypi/telnetsrv/0.4)
* SimpleJson (https://github.com/simplejson/simplejson)
* Cryptography (https://cryptography.io/en/latest/)

# So how does it work together

Unfortunately, for all the new the mu client remains a strong force in the mu game world. They're even mentioned in the github documentation for Telnetlib3. This isn't likely change, but what is changing is the desire for something new. Anything new needs to be able to seamlessly integrate with the old. The thought process then has to begin there. Where do we go then?

First, you support telnet. There's no real reason to do this. It's not like a Mu game needs to support telnet anymore. Redis (Or even Mongodb or any database) could be used to serve an entire game through a browser with no telnet and only javascript. However, the old school faction is pretty big.

Second, you break telnet down to just telnet. Time to stop thinking about it as a Mu server and start thinking about it as just a telnet protocol connecting to a type of server. Then you find a way to make the telnet integrate with everything else.

Third, you use redis as a message dispatcher, because it's actually already made for that and does surprisingly well.

Fourth, Profit.

So basically, you can run a server that accepts connections from telnet clients, a web client, a mobile client, someone using the rest api or someone using the OOB channel to make their own client and they can all communicate because of Redis being the basis for that message dispatching. 

# So how does it game

Since everything is given an ID, the information on a Mu server is naturally suited to Hashes. Lots and Lots of hashes. That's a simplification. The hardest negotiation between the platforms is color. Telnet uses special control codes. The web uses another set. Everything else is just text. Formatting is universal. A space is a space is a space. (Kill the tabs.)

