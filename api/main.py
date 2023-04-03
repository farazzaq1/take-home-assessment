from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
import random

app = FastAPI()
api_calls = []

# Authorization Function
def authenticate_user(username: str, password: str):
    valid_username = "myusername"
    valid_password = "mypassword"
    if username == valid_username and password == valid_password:
        return True
    return False

# Jumble API
@app.get("/jumble/{word}")
async def jumble_word(word: str, authorized: bool = Depends(authenticate_user)):
    if not authorized:
        raise HTTPException(status_code=401, detail="Unauthorized")
    jumbled_word = "".join(random.sample(word, len(word)))
    api_calls.append({word: jumbled_word})
    return {"jumbled_word": jumbled_word}

# Audit API
@app.get("/audit")
async def get_api_calls(authorized: bool = Depends(authenticate_user)):
    if not authorized:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"api_calls": api_calls[-10:]}
