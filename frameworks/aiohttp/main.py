from aiohttp import web


async def hello(request):
    return web.Response(text="Hello aiohttp!")


async def run_app():
    app = web.Application()
    app.router.add_get('/', hello)
    return app
