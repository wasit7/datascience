from aiohttp import web
app = web.Application()

async def index(request):
    res = {"key": "value", "my": "data"}
    return web.json_response(res)
    
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)