from bottle import Bottle, run

app = Bottle()


@app.route('/')
def hello():
    return "Hello bottle"


if __name__ == '__main__':
    run(app, host='localhost', port=8080, server='gunicorn', debug=False)
