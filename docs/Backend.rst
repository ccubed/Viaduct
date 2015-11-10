Stonework Class
================

.. py:module:: Backend
Module for the Stonework Redis Backend.

    ..  py:class:: Stonework
    Class for the Redis Backend.

        ..  py:attribute:: rc
        Holds the dictionary of the Redis DB connections and connection pools.
        Dictionary in form { Connection Pool, Connection Manager, Connection }.

        .. py:classmethod:: addhash(hashid : integer, data : dictionary, db : integer)
        Add a hash to a db in redis. Data is a dictionary with key-value pairs.

        .. py:classmethod:: addpair(key, value, db)
        Add a key to redis with the given value on the specified db. Key and value can be any type.

        .. py:classmethod:: gethash(hashid : integer, data, db, return_format='json')
        Get the value of a specific key stored in a hash. You can also pass 'all' to data to get all the keys and values.
        Return_format controls how the system returns the data. If passed 'python' it will return the data as a python dictionary.
        'text' will return the data in a text format. 'json' returns the data as correctly formatted json. If passed 'all'
        the data is returned as a dictionary of byte objects for python, a json array for json and new line separated key
        value pairs for text. On text and json the byte objects are converted to utf-8 encoded text first.

        .. py:classmethod:: getpair(key, db)
        Get the value of key stored on db. Returned as utf-8 encoded text.

        .. py:classmethod:: redisdump()
        Tell redis to initate a bgsave and dump its data to the disk.

        .. py:classmethod:: killkey(key, db)
        This sets the expire time on key to 1 on the given db essentially deleting it instantly. +/- 1 millisecond.