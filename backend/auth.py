import os
from fastapi import Header, HTTPException
from jose import jwt

SECRET = os.getenv("JWT_SECRET", "dev-secret")
ALGO = os.getenv("JWT_ALGO", "HS256")

def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split()[1]
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        return {"sub": payload["sub"]}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
