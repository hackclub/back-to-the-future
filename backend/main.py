import json
import os
import re
from typing import Annotated, Any, Dict
import httpx
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("./backend/.env")
load_dotenv(dotenv_path=dotenv_path)

app = FastAPI()
security_scheme = HTTPBearer()

DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)

HACKCLUB_CLIENT_ID = os.getenv("CLIENT_ID", "your_client_id")
HACKCLUB_CLIENT_SECRET = os.getenv("CLIENT_SECRET", "your_client_secret")

HACKCLUB_TOKEN_URL = "https://auth.hackclub.com/oauth/token"
HACKCLUB_ME_URL = "https://auth.hackclub.com/api/v1/me"

def get_user_filepath(user_id: str) -> str:
    safe_id = re.sub(r"[^a-zA-Z0-9_-]", "", str(user_id))
    return os.path.join(DATA_DIR, f"{safe_id}.json")

def read_user_file(user_id: str) -> dict:
    filepath = get_user_filepath(user_id)
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def write_user_file(user_id: str, data: dict) -> None:
    filepath = get_user_filepath(user_id)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security_scheme)]
) -> dict:
    token = credentials.credentials

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                HACKCLUB_ME_URL,
                headers={"Authorization": f"Bearer {token}"},
                timeout=10.0,
            )
        except httpx.RequestError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Unable to reach Hack Club Auth service",
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired Hack Club OAuth token",
            )

        user_data = response.json()

    identity = user_data.get("identity", user_data)
    user_id = identity.get("id")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile missing unique ID",
        )

    return {"user_id": str(user_id), "identity": identity}

@app.get("/")
async def root():
    return "do people still mew these days,v0_0"


@app.get("/token")
async def exchange_token(code: str, redirect_uri: str):
    async with httpx.AsyncClient() as client:
        token_response = await client.post(
            HACKCLUB_TOKEN_URL,
            data={
                "client_id": HACKCLUB_CLIENT_ID,
                "client_secret": HACKCLUB_CLIENT_SECRET,
                "redirect_uri": redirect_uri,
                "grant_type": "authorization_code",
                "code": code,
            },
        )

        print({
                "client_id": HACKCLUB_CLIENT_ID,
                "client_secret": HACKCLUB_CLIENT_SECRET,
                "redirect_uri": redirect_uri,
                "grant_type": "authorization_code",
                "code": code,
            })

        print(token_response);

        if token_response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Token exchange failed: {token_response.text}",
            )

        token_data = token_response.json()
        access_token = token_data.get("access_token")

        # Fetch profile to identify the user
        me_response = await client.get(
            HACKCLUB_ME_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        
        if me_response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to fetch user identity",
            )

        identity = me_response.json().get("identity", me_response.json())
        user_id = str(identity.get("id"))

        # Initialize JSON storage for this user if it doesn't exist
        user_file = read_user_file(user_id)
        if not user_file:
            initial_data = {
                "email": identity.get("email"),
                "slack_id": identity.get("slack_id"),
                "app_data": {},
            }
            write_user_file(user_id, initial_data)

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user_id,
            "profile": identity,
        }


@app.get("/data")
async def get_data(current_user: Annotated[dict, Depends(get_current_user)]):
    user_id = current_user["user_id"]
    file_contents = read_user_file(user_id)
    return file_contents


@app.post("/data")
async def set_data(
    payload: Dict[Any, Any],
    current_user: Annotated[dict, Depends(get_current_user)],
):
    user_id = current_user["user_id"]

    user_file = read_user_file(user_id) or {"user_id": user_id}
    user_file["app_data"] = payload

    write_user_file(user_id, user_file)

    return {"status": "success", "saved_data": user_file}