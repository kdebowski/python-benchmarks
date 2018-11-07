from weppy import App
app = App(__name__)


@app.route("/")
def hello():
    return "Hello weppy!"


if __name__ == "__main__":
    app.run()