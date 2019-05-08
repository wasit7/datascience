from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

async def js(request):
    return web.FileResponse('./socket.io.js')

@sio.on('channel_a')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(type(message),message)
    await sio.emit('channel_b', message)

app.router.add_get('/', index)
app.router.add_get('/socket.io.js', js)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)