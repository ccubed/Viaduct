from flask import *
from Backend import *

api = Blueprint('api', __name__, template_folder='templates', static_folder='static')


# API Routes
# Players
@api.route('/players/create', methods=['POST'])
def api_create_player():
    if 'name' in request.form and 'password' in request.form:
        # Stuff
    else:
        resp = make_response(json.dumps({'Status': 'False', 'Details': 'Did not pass name or password in POST data.'}), 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp

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


@api.route('/comms/send')
def api_send_channel_message(channel):
    return 'Send a message to a channel'


@api.route('/comms/leave/<channel>')
def api_leave_channel(channel):
    return 'Leave a channel'


# Mails
@api.route('/mails')
def api_list_mails():
    return 'List mails'


@api.route('/mails/<number>')
def api_get_mail(number):
    return 'Get contents of a specified mail'


@api.route('/mails/send')
def api_send_mail(to, title, message):
    return 'Send a mail to someone'


@api.route('/mails/delete/<number>')
def api_delete_mail(number):
    return 'Delete a mail'


@api.route('/mails/reply/')
def api_reply_mail():
    return 'Reply to a mail'


@api.route('/mails/forward/')
def api_forward_mail():
    return 'Forward a mail'


# Keys (API Keys)
@api.route('/keys/<permissions>')
def get_key(permissions):
    return 'Get a one time password'


@api.route('/keys/activate')
def activate_key():
    return 'Activate an API key with a OTPW'


@api.route('/keys/deactivate')
def deactivate_key():
    return 'Deactivate an API key'


@api.route('/keys/list')
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
