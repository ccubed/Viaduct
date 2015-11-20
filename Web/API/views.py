from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates', static_folder='static')


# API Routes
# Players
@api.route('/players/create/<name>/<password>')
def api_create_player(name, password):
    if len(password) < 6:
        return json.dumps({'Result': 'Error', 'Details': 'Password must be at least 6 characters.'})
    else:
        return json.dumps({'Result': 'Success', 'Details': 'Created Character ' + name})


# Game
@api.route('/game/who')
def api_who():
    return 'Who is on'


@api.route('/game/move/<direction>')
def move(direction):
    return 'Move player direction'


@api.route('/game/say/<text>')
def say(text):
    return 'Say something'


@api.route('/game/pose/')
def pose():
    return 'Process a pose'


# Comms
@api.route('/comms/channels')
def api_list_channels():
    return 'List of channels'


@api.route('/comms/join/<channel>')
def api_join_channel(channel):
    return 'Join a channel'


@api.route('/comms/get/<channel>')
def api_get_channel_messages(channel):
    return 'Stored messages for channel'


@api.route('/comms/send/<channel>/<message>')
def api_send_channel_message(channel, message):
    return 'Send a message to a channel'


@api.route('/comms/leave/<channel>')
def api_leave_channel(channel):
    return 'Leave a channel'


# Mails
@api.route('/mails')
def api_list_mails():
    return 'List mails'


@api.route('/mail/<number>')
def api_get_mail(number):
    return 'Get contents of a specified mail'


@api.route('/mail/send/<to>/<title>/<message>')
def api_send_mail(to, title, message):
    return 'Send a mail to someone'


# Key (API Keys)
@api.route('/key/<permissions>')
def get_key(permissions):
    return 'Get a one time password'


@api.route('/key/activate')
def activate_key():
    return 'Activate an API key with a OTPW'


@api.route('/key/deactivate')
def deactivate_key():
    return 'Deactivate an API key'


@api.route('/key/list')
def list_keys():
    return 'List of API Keys'


# Streams
@api.route('/streams/room/<action>')
def room_stream(action):
    return 'Subscribe or unsubscribe from the stream of room actions for a player'


@api.route('/streams/chans/<action>')
def chan_stream(action):
    return 'Subscribe or unsubscribe from the stream of channel actions for a player'


@api.route('/streams/api/<action>')
def api_stream(action):
    return 'Subscribe or unsubscribe from the stream of API actions for a player'
