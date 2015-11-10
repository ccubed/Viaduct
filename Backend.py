# Handles our redis interactions so we can control thread safe interoperability.

import redis, simplejson as json


class Stonework:
    def __init__(self):
        self.rc = []
        for i in range(15):
            tempcp = redis.ConnectionPool(host='localhost', port=6379, db=i)
            tempcpr = redis.Redis(connection_pool=tempcp)
            self.rc.append([tempcp, tempcpr, redis.StrictRedis(host='localhost', port=6379, db=i)])

    # Add data to a hash or edit what's there. Data should be a dictionary.
    def addhash(self, hashid, data, db):
        if 15 >= db >= 0:
            if hashid == 0:
                return 0
            else:
                for k, v in data.items():
                    self.rc[db][2].hset(hashid, k, v)
                if db == 2:
                    # Comms are only saved for 48 hours
                    self.rc[db][2].expire(hashid, 172800)
                elif 10 <= db < 15:
                    # The log DBs keep log entries for 4 days
                    self.rc[db][2].expire(hashid, 345600)
                elif db == 15:
                    # The dbus keeps messages for 1 hour
                    self.rc[db][2].expire(hashid, 3600)
                return 1
        else:
            return 0

    # Create a key value pair. These are temporary and only exist in DB 8.
    def addpair(self, key, value, db):
        if 15 >= db >= 0:
            self.rc[db][2].set(key, value)
            return 1
        else:
            return 0

    # Get data from a hash and return it in the requested format.
    def gethash(self, hashid, data, db, return_format='json'):
        if 15 >= db >= 0:
            if return_format == 'json':
                if data == 'all':
                    return json.dumps(self.rc[db][2].hgetall(hashid))
                else:
                    return json.dumps(str(self.rc[db][2].hget(hashid,data), 'utf-8'))
            elif return_format == 'python':
                if data == 'all':
                    return self.rc[db][2].hgetall(hashid)
                else:
                    return str(self.rc[db][2].hget(hashid, data), 'utf-8')
            elif return_format == 'text':
                if data == 'all':
                    unfdata = self.rc[db][2].hgetall(hashid)
                    retstring = ""
                    for k, v in unfdata.items():
                        retstring = str(k, 'utf-8') + ": " + str(v, 'utf-8') + '\n'
                    return retstring
                else:
                    unfdata = str(self.rc[db][2].hget(hashid, data), 'utf-8')
                    return unfdata
        else:
            return 'Error'

    # Get the value for a key and delete the key. Remember, temporary.
    def getpair(self, key, db):
        if 15 >= db >= 0:
            return str(self.rc[db][2].get(key), 'utf-8')
        else:
            return 'Error'

    # Dump redis to disk. This is an asynchronous task.
    def redisdump(self):
        self.rc[0][2].bgsave()
        return 1

    # Kill a pair or hash
    def killkey(self, key, db):
        if 15 >= db >= 0:
            self.rc[db][2].expire(key,1)
            return 1
        else:
            return 0
