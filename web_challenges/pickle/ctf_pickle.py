from flask import Flask
from flask import request
from flask import make_response
import base64
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    cookie = {'type': 'pickles', 'user_name': 'user'}
    encoded_cookie = base64.b64encode(pickle.dumps(cookie))

    green_pickle = request.cookies.get('greenPickle')

    if green_pickle is not None:
        green_pickle = pickle.loads(base64.b64decode(green_pickle))
        user_name = green_pickle.get('user_name')
        if user_name.lower() == 'admin':
            return "Flag{pickles_are_great}"

    resp = make_response("Welcome to my site,"
    "sorry it's still under construction..."
    "admins only")
    resp.set_cookie('greenPickle', encoded_cookie)
    return resp


@app.route('/admin')
def admin():
    return "No flag here"

if __name__ == "__main__":
    app.run(port=8888)
    #app.run()
