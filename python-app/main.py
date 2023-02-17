from deta import Base, Drive
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI()
# Connect to a Base to store user data
users_db = Base("users")
# Connect to a Drive to store user avatars
avatars_drive = Drive("avatars")


@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World!"})


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    # Get the user from the Base
    user = users_db.get(user_id)
    # If the user doesn't exist, return a 404 error
    if user is None:
        raise HTTPException(status_code=404)
    return user


@app.post("/users")
async def create_user(user: dict):
    try:
        # Insert the user into the Base. If the user already exists, this will raise an exception
        response = users_db.insert(user, user["id"])
        status = 201
    except Exception as exc:
        # If the user already exists, return a 409 error
        response = {"message": str(exc)}
        status = 409
    return JSONResponse(response, status_code=status)


@app.get("/users/{user_id}/avatar")
async def get_avatar(user_id: str):
    # Get the avatar from the Drive
    avatar = avatars_drive.get(f"{user_id}.png")
    # If the avatar doesn't exist, return a 404 error
    if avatar is None:
        raise HTTPException(status_code=404)
    return Response(avatar, media_type="image/png")


@app.post("/users/{user_id}/avatar")
async def upload_avatar(request: Request, user_id: str):
    # Get the avatar from the request body
    file = await request.body()
    # Upload the avatar to the Drive
    return avatars_drive.put(f"{user_id}.png", file)
