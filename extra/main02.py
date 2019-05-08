from aiohttp import web
app = web.Application()

async def index(request):
    with open('index02.html') as f:
        return web.Response(text=f.read(), content_type='text/html')
    
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)