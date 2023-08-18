import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Fist page'



if __name__ == '__main__':
    app.run(debug=True)


