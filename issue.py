import os
import subprocess
from flask import Flask, request, abort

app = Flask(__name__)

open_sound = dict()
for fn in os.listdir('opened'):
    open_sound[os.path.splitext(fn)[0]] = os.path.join('opened', fn)

close_sound = dict()
for fn in os.listdir('closed'):
    close_sound[os.path.splitext(fn)[0]] = os.path.join('closed', fn)


@app.route('/github_issues', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(data)
        if data.get('action') == 'opened':
            user = data['issue']['user']['login']
            sound_file = open_sound.get(user, open_sound['default'])
            subprocess.run(['omxplayer', sound_file])
            print('open', user, sound_file)
        elif data['action'] == 'closed':
            user = data['issue']['assignee']
            sound_file = close_sound.get(user, close_sound['default'])
            subprocess.run(['omxplayer', sound_file])
            print('close', user, sound_file)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5567, debug=True)

