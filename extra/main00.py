from aiohttp import web
app = web.Application()

async def index(request):
    return web.Response(text="Hello World!!")

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)