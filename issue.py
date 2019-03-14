import os
import subprocess
from threading import Thread
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

open_sound = dict()
for fn in os.listdir('opened'):
    open_sound[os.path.splitext(fn)[0]] = os.path.join('opened', fn)

close_sound = dict()
for fn in os.listdir('closed'):
    close_sound[os.path.splitext(fn)[0]] = os.path.join('closed', fn)


def play_sound(sound_file):
    subprocess.run(['omxplayer', '--no-keys', '--no-osd', sound_file])


@app.route('/github_issues', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        if data.get('action') == 'opened':
            user = data['issue']['user']['login']
            sound_file = open_sound.get(user, open_sound['default'])
            Thread(target=play_sound, args=(sound_file,)).start()
            print('open', user, sound_file)
        elif data['action'] == 'closed':
            user = data['issue']['assignee']
            if user is not None:
                user = user['login']
            sound_file = close_sound.get(user, close_sound['default'])
            Thread(target=play_sound, args=(sound_file,)).start()
            print('close', user, sound_file)
        return jsonify({'status':'success'}), 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5567, debug=True)

