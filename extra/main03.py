from aiohttp import web
app = web.Application()

app.router.add_static('/static/',
    path='static',
    name='static')

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)