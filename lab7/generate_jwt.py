#!/usr/bin/env python3
import jwt
import time

USER = ""
SECRET = "" 

if __name__ == "__main__":
    payload = {
        "sub": USER,
        "iat": int(time.time()),
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")
    print(token)