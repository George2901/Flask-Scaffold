import waitress
from flask import Flask, send_from_directory
from flask import request

app = Flask(__name__)


# app.debug = True

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    match request.method:
        case 'GET':
            return send_from_directory('pages', 'index.html'), 200
        case 'POST':
            return send_from_directory('pages', 'index.html'), 200


@app.route('/css/<path>', methods=['GET'])
def css(path):
    return send_from_directory('pages/css', '', path), 200


@app.route('/imgs/<path>', methods=['GET'])
def img(path):
    return send_from_directory('pages/imgs', '', path), 200


@app.route('/js/<path>')
def js(path):
    return send_from_directory('pages/js', '', path), 200


@app.errorhandler(404)
@app.route('/error.html', methods=['GET'])
def error(self):
    return send_from_directory('./pages', 'error.html'), 404


if __name__ == '__main__':
    try:
        waitress.serve(app)
    except:
        app.run(port=8080)
