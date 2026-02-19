import argparse, os
from jose import jwt

SECRET = os.getenv("JWT_SECRET", "dev-secret")
ALGO = os.getenv("JWT_ALGO", "HS256")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--sub', required=True, help='subject/user id')
    args = p.parse_args()
    print(jwt.encode({"sub": args.sub}, SECRET, algorithm=ALGO))
