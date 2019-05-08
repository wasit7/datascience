from aiohttp import web
import socketio
import numpy as np
import json

app = web.Application()
sio = socketio.AsyncServer()
sio.attach(app)

async def index(request):
    with open('index05.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

async def gendata(request):
    data=['data']
    for i in range(10):
        data.append(np.random.randint(1000))    
    print(data)
    await sio.emit('channel_b', json.dumps(data) )
    return web.Response(text="Data is generated")

app.router.add_get('/', index)
app.router.add_get('/gendata', gendata)
app.router.add_static('/static/', path='static', name='static')

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)