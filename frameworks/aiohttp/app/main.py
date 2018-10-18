from aiohttp import web


async def index(request):
    return web.Response(text="Welcome home!")


async def run_app():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host='0.0.0.0', port='8080')