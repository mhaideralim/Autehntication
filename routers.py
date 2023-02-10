from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from database import User
from main import app
from db_connection import user_data
from database import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    print (user)


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user