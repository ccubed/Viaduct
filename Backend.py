import redis
import simplejson as json


def addhash(hashid, data, db):
    if 15 >= db >= 0:
        rc = redis.StrictRedis(db=db)
        if hashid == 0:
            rc.connection_pool.disconnect()
            return 0
        else:
            for k, v in data.items():
                rc.hset(hashid, k, v)
            if db == 2:
                # Comms are only saved for 48 hours
                rc.expire(hashid, 172800)
            elif db == 15:
                # The dbus keeps messages for 1 hour
                rc.expire(hashid, 3600)
            rc.connection_pool.disconnect()
            return 1
    else:
        return 0


# Create a key value pair. These are temporary and only exist in DB 8.
def addpair(key, value, db):
    if 15 >= db >= 0:
        rc = redis.StrictRedis(db=db)
        rc.set(key, value)
        rc.connection_pool.disconnect()
        return 1
    else:
        return 0


# Get data from a hash and return it in the requested format.
def gethash(hashid, data, db, return_format='json'):
    if 15 >= db >= 0:
        rc = redis.StrictRedis(db=db)
        if return_format == 'json':
            if data == 'all':
                temp = json.dumps(rc.hgetall(hashid))
                rc.connection_pool.disconnect()
                return temp
            else:
                temp = json.dumps(str(rc.hget(hashid, data), 'utf-8'))
                rc.connection_pool.disconnect()
                return temp
        elif return_format == 'python':
            if data == 'all':
                temp = rc.hgetall(hashid)
                rc.connection_pool.disconnect()
                return temp
            else:
                temp = str(rc.hget(hashid, data), 'utf-8')
                rc.connection_pool.disconnect()
                return temp
        elif return_format == 'text':
            if data == 'all':
                unfdata = rc.hgetall(hashid)
                retstring = ""
                rc.connection_pool.disconnect()
                for k, v in unfdata.items():
                    retstring = str(k, 'utf-8') + ": " + str(v, 'utf-8') + '\n'
                return retstring
            else:
                unfdata = str(rc.hget(hashid, data), 'utf-8')
                rc.connection_pool.disconnect()
                return unfdata
    else:
        return 'Error'


# Get the value for a key and delete the key. Remember, temporary.
def getpair(key, db):
    if 15 >= db >= 0:
        # noinspection PyBroadException
        try:
            rc = redis.StrictRedis(db=db)
            temp = str(rc.get(key), 'utf-8')
            rc.connection_pool.disconnect()
            return temp
        except:
            return 'Error - Key not found'
    else:
        return 'Error - Only 15 DBs'


# Dump redis to disk. This is an asynchronous task.
def redisdump():
    rc = redis.StrictRedis()
    rc.bgsave()
    rc.connection_pool.disconnect()
    return 1


# Kill a pair or hash
def killkey(key, db):
    if 15 >= db >= 0:
        rc = redis.StrictRedis(db=db)
        rc.expire(key, 1)
        rc.connection_pool.disconnect()
        return 1
    else:
        return 0
