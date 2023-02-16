from deta import Deta
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI()
deta = Deta()
users_db = deta.Base("users")
avatars_drive = deta.Drive("avatars")


@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World!"})


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user


@app.post("/users")
async def create_user(user: dict):
    try:
        response = users_db.insert(user, user["id"])
        status = 201
    except Exception as exc:
        response = {"message": str(exc)}
        status = 409
    return JSONResponse(response, status_code=status)


@app.get("/users/{user_id}/avatar")
async def get_avatar(user_id: str):
    avatar = avatars_drive.get(f"{user_id}.png")
    if avatar is None:
        raise HTTPException(status_code=404)
    return Response(avatar, media_type="image/png")


@app.post("/users/{user_id}/avatar")
async def upload_avatar(request: Request, user_id: str):
    file = await request.body()
    return avatars_drive.put(f"{user_id}.png", file)
