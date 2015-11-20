API
===
This will be a listing of the calls available to the RESTful API. For now this is empty but exists as a placeholder.
The one thing all the API calls share in common is that your API key and the player's Hash ID must be placed in the request header.

.. http:any:: /api/*

   All the API calls.

   :>header x-api-key: Your API Key
   :>header x-hash: The current player's Hash ID

Sections
========
The REST API is separated into various sections in the code file to allow for easier navigation and finding of similar funcitons.
This is a list of the sections.

* :ref:`Players <Players>` - End points relating to creation and modification of player data.

    1. :ref:`Create <Players-Create>` - Make a new Player through the API.

* :ref:`Game <Game>` - End points related to built in game. Such as say, pose or movement.

    1. :ref:`Who <Game-Who>` - Who is on?
    2. :ref:`Move <Game-Move>` - Move a player through rooms using the API.
    3. :ref:`Say <Game-Say>` - Make a player say something to a room through the API.
    4. :ref:`Pose <Game-Pose>` - Make a player pose something to a room through the API.

* Comms - End points related to channels or communication systems in game. Such as @channel, +comm, +radio, etc depending.
* Mails - End points related to in game mails.
* Key - End points related to player API Key management.
* Streams - End points for developers to subscribe to various dbus event streams.

API Documentation
=================
.. _Players:

.. _Players-Create:
.. http:post:: /api/players/create/

   Create a player with the specified username and password.

   :form name: Name of the new player
   :form password: Password for the new player

   :statuscode 200: No Error
   :statuscode 404: User not created

   :resheader Content-Type: application/json
   :>jsonarr boolean status: If successful, return True
   :>jsonarr string id: and then the new Player's Hash ID
   :>jsonarr boolean status: If unsuccessful, return False
   :>jsonarr string details: and then the Error Details

.. _Game:
.. _Game-Who:
.. http:get:: /api/game/who

   Get a list of currently connected players. Returns an array.

   :statuscode 200: All good
   :statuscode 404: The game is down

   :resheader Content-Type: application/json
   :>jsonarr string name: Name of Player
   :>jsonarr string uptime: Player's Total Connection Time. Formatted in seconds.
   :>jsonarr string idle: Player's idle time. Formatted in seconds.
   :>jsonarr boolean status: If game is down return false

.. _Game-Move:
.. http:get:: /api/game/move/(string:direction)

   Attempt to move player direction.

   :param direction: Direction to attempt to move player.
   :type direction: String

   :statuscode 200: All good
   :statuscode 404: That direction wasn't good

   :resheader Content-Type: application/json
   :>jsonarr string room: Room Name
   :>jsonarr string players: Space separated list of other players in the room or None
   :>jsonarr string objects: Space separated list of other things in the room or None
   :>jsonarr string description: Room Description
   :>jsonarr array exits: Array in form of 'direction':'name'
   :>jsonarr boolean status: If direction was bad this is returned as false
