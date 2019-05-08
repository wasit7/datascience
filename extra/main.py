from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('channel')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(type(message),message)
    # await a successful emit of our reversed message
    # back to the client
    await sio.emit('message', message)

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)