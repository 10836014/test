from flask import *
from test import app as application
app = Flask(__name__)


@app.route('/')
def index():
    return '<center><h1>Hello Flask-test</h1></center>'


if __name__ == '__main__':
    app.run(debug=True)

