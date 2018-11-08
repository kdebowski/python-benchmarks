from sanic import Sanic
from sanic.response import text

app = Sanic()


@app.route("/")
async def test(request):
    return text('hello sanic')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, workers=4)
