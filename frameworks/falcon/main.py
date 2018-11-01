import falcon


class HelloResource(object):

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = ('Hello falcon')


app = falcon.API()
hello = HelloResource()
app.add_route('/', hello)
