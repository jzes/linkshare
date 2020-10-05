from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/open', methods=['POST'])
def open_link():
    link = request.json['link']
    os.system('google-chrome {}'.format(link))
    return 'opened'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)