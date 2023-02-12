from deta import Deta
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse, Response


app = FastAPI()
db = Deta().Base("users")
drive = Deta().Drive("avatars")


@app.get("/")
def root():
    return JSONResponse({"message": "Hello World"})

@app.post("/users")
def create_user(user: dict):
    try:
        resp = db.insert(user, user["id"])
        resp.status = 201
    except Exception as e:
        resp = {"message": str(e)}
        resp.status = 409
    return JSONResponse(resp, status_code=resp.status)

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return db.get(user_id)

@app.post("/users/{user_id}/avatar")
async def upload_avatar(req: Request, user_id: str):
    file = await req.body()
    return drive.put(f'{user_id}.png', file)

@app.get("/users/{user_id}/avatar")
def get_avatar(user_id: str):
    return Response(drive.get(f'{user_id}.png'), media_type="image/png")
