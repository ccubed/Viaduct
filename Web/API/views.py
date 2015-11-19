# API Routes
# Players
@app.route('/api/players/create/<name>/<password>')
def api_create_player(name, password):
    if len(password) < 6:
        return json.dumps({'Result': 'Error', 'Details': 'Password must be at least 6 characters.'})
    else:
        return json.dumps({'Result': 'Success', 'Details': 'Created Character ' + name})


# Game
@app.route('/api/game/who')
def api_who():
    return 'Who is on'


# Comms
@app.route('/api/comms/channels')
def api_list_channels():
    return 'List of channels'


@app.route('/api/comms/join/<channel>')
def api_join_channel(channel):
    return 'Join a channel'


@app.route('/api/comms/get/<channel>')
def api_get_channel_messages(channel):
    return 'Stored messages for channel'


@app.route('/api/comms/send/<channel>/<message>')
def api_send_channel_message(channel, message):
    return 'Send a message to a channel'


@app.route('/api/comms/leave/<channel>')
def api_leave_channel(channel):
    return 'Leave a channel'


# Mail
@app.route('/api/mails')
def api_list_mails():
    return 'List mails'


@app.route('/api/mail/<number>')
def api_get_mail(number):
    return 'Get contents of a specified mail'


@app.route('/api/mail/send/<to>/<title>/<message>')
def api_send_mail(to, title, message):
    return 'Send a mail to someone'
