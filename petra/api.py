from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def method():
    pass


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
