#!/usr/bin/env python3
from fastapi import FastAPI, Depends, Response
from pydantic import BaseModel, ConfigDict

import hvac
import http
import os

import uvicorn

app = FastAPI()

OPENBAO_URL = os.getenv("OPENBAO_URL")
OPENBAO_TOKEN = os.getenv("OPENBAO_TOKEN")

class PostData(BaseModel):
    value: str

@app.post("/secret/{path}")
def post_secret(path: str, data: PostData):
    # TODO: Save data here
    return Response(status_code=http.HTTPStatus.NO_CONTENT)

@app.get("/secret/{path}")
def read_secret(path: str):
    openbao_client: hvac.Client = hvac.Client(url=OPENBAO_URL, token=OPENBAO_TOKEN)
    # TODO: Retrieve the value from OpenBao
    # openbao_client = hvac.Client(...)
    # value = openbao_client.secrets.kv.v2.read_secret_version()
    SECURE_VALUE = ...
    return {"secure_value": SECURE_VALUE}

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=443,
        # TODO: Add key file
        ssl_keyfile=...,
        # TODO: Add cert file
        ssl_certfile=...,
        # TODO: Add CA certs
        ssl_ca_certs=...
    )