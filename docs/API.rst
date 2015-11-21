API
===
This will be a listing of the calls available to the RESTful API. For now this is empty but exists as a placeholder.
There are some things all the API calls share in common. One is that your API key and the player's Hash ID must be placed in the request header.
Another is that status codes all have the same meanings.

.. http:any:: /api/*

   All the API calls.

   :>header x-api-key: Your API Key
   :>header x-hash: The current player's Hash ID

   :statuscode 200: This always means ok.
   :statuscode 204: This means that the server processed your request, but what you wanted doesn't exist.
   :statuscode 400: Read the documentation and resend the API request the right way.
   :statuscode 404: This means the game is down.

As a note, Status code 204 will never return content. This is in line with RFC2616 which states that the browser should (should mind you) stop accepting input after the first line break - IE after the header.

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

* :ref:`Comms <Comms>` - End points related to channels or communication systems in game. Such as @channel, +comm, +radio, etc depending.

    1. :ref:`Channels <Comms-Channels>` - List of Channels available
    2. :ref:`Join <Comms-Join>` - Join a Channel
    3. :ref:`Get <Comms-Get>` - Get a list of stored messages for a Channel
    4. :ref:`Send <Comms-Send>` - Send a message to a Channel
    5. :ref:`Leave <Comms-Leave>` - Leave a Channel

* :ref:`Mails <Mails>` - End points related to in game mails.

    1. :ref:`Mails <Mails-List>` - List Mails
    2. :ref:`Read <Mails-Read>` - Read a Mail
    3. :ref:`Send <Mails-Send>` - Send a mail
    4. :ref:`Delete <Mails-Delete>` - Delete a Mail
    5. :ref:`Reply <Mails-Reply>` - Reply to a mail. This is basically a shorter send.
    6. :ref:`Forward <Mails-Forward>` - Forward a mail.

* :ref:`Keys <Keys>` - End points related to player API Key management.

    1. :ref:`Keys <Keys-Make>` - Ask player to approve a key
    2. :ref:`Activate <Keys-Activate>` - Activate a key once player has approved and given you a One Time Password
    3. :ref:`Deactivate <Keys-Deactivate>` - Deactivate a key
    4. :ref:`List <Keys-List>` - List API Keys

* :ref:`Streams <Streams>` - End points for developers to subscribe to various dbus event streams.

    1. :ref:`Room <Streams-Room>` - Room Action Stream
    2. :ref:`Chans <Streams-Chans>` - Channel Action Stream
    3. :ref:`Api <Streams-Api>` - API Action Stream

API Documentation
=================
.. _Players:

.. _Players-Create:
.. http:post:: /api/players/create

   Create a player with the specified username and password. This API call breaks the rules because it does not require you to submit an API key or a player Hash. Instead it will return a player Hash to you. You should then ask them to give you an API key.

   :form name: Name of the new player
   :form password: Password for the new player

   :statuscode 200: No Error
   :statuscode 400: You didn't send the request with all the required data.
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

.. _Game-Say:
.. http:get:: /api/game/say(string:message)

   Say something to a room.

   :param message: What to say.
   :type message: String

   :statuscode 200: Message processed to room.
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr boolean status: True or False depending on success.

.. _Game-Pose:
.. http:post:: /api/game/pose

   Send a pose to a room.

   :form text: Text of the pose.

   :statuscode 200: Pose processed to room.
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr boolean status: True or False depending on success.

.. _Comms:
.. _Comms-Channels:
.. http:get:: /api/comms/channels

   Get a list of available channels.

   :statuscode 200: List is being returned.
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr string name: Channel Name

.. _Comms-Join:
.. http:get:: /api/comms/join/(string:channel)

   Join player to a comm channel.

   :param channel: What channel to join.
   :type channel: String

   :statuscode 200: All good.
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr boolean status: True or False depending on success.

.. _Comms-Get:
.. http:get:: /api/comms/get/(string:channel)

   Get a list of all currently stored messages on channel.

   :param channel: What channel are we grabbing messages for.
   :type channel: String

   :statuscode 200: All good.
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr string name: Name of Player who sent the message.
   :>jsonarr string message: Message text.
   :>jsonarr date posted: When was this message sent.

.. _Comms-Send:
.. http:post:: /api/comms/send

   Send a message to a channel.

   :form channel: What channel.
   :form message: What is the message.

   :statuscode 200: Ok
   :statuscode 404: Game is down.

   :resheader Content-Type: application/json
   :>jsonarr boolean status: True or False depending on success

.. _Comms-Leave:
.. http:get:: /api/comms/leave/(string:channel)

   Leave a channel.

   :param channel: Which channel?
   :type channel: String

   :statuscode 200: Ok
   :statuscode 404: Game is down.

   :reshead Content-Type: application/json
   :>jsonarr boolean status: True or False depending on success.

.. _Mails:
.. _Mails-List:
.. http:get:: /api/mails

   Get a list of all of player's mails.

   :statuscode 200: Ok
   :statuscode 404: Game is down.

   :reshead Content-Type: application/json
   :>jsonarr string id: Number of Mail
   :>jsonarr string title: Title of mail
   :>jsonarr string from: Player it's from

.. _Mails-Read:
.. http:get:: /api/mails/(integer:number)

   Get the contents of a specific mail. Note that this does not return the title or from. You should already have that.

   :statuscode 200: Ok
   :statuscode 204: The game is up, but that mail doesn't exist.
   :statuscode 404: Game is down.

   :reshead Content-Type: application/json
   :>jsonarr string contents: The message body.

.. _Mails-Send:
.. http:post:: /api/mails/send

   Send a mail.

   :form to: Player name to send the message to. Server will handle name to hash conversion.
   :form title: Mail Title. AKA Subject if you prefer.
   :form message: Mail body text.

   :statuscode 200: Mail sent.
   :statuscode 204: The game is up and we understood your request, but that player doesn't exist.
   :statuscode 404: Game is down.