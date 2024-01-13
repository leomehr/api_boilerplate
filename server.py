from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Greeting(BaseModel):
    name: str
    msg: str

msgs = {
    'hello': 'Hello! 👋'
}

def response(msg: str, ok: bool) -> dict:
    return {
        'msg': msg,
        'ok': ok
    }

@app.get('/hello')
async def get_hello():
    return response(msgs['hello'], True)

@app.get('/msg/{msg_id}')
async def get_msg(msg_id: str):
    if msg_id in msgs:
        return response(msgs[msg_id], True)
    return response('', False)

@app.get('/msgs')
async def get_msgs(limit: int = 3):
    return dict((k, msgs[k]) for k in list(msgs.keys())[:limit])

@app.put('/update_hello')
async def update_hello(new_hello: str):
    msgs['hello'] = new_hello
    return {'ok': True}

@app.post('/new_greeting')
async def new_greeting(greeting: Greeting):
    if greeting.name in msgs:
        return {'ok': False}

    msgs[greeting.name] = greeting.msg
    return {'ok': True}
