from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello Pyramid!')


with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
