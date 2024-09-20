import json
import os

import httpx
import requests
from dotenv import load_dotenv
from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse

load_dotenv()

router = APIRouter()

@router.post("/generate_presentation", response_class=JSONResponse)
async def generate_presentation(
    user_input: str = Form(..., description="Input text for the presentation."),
    theme_color: str = Form(..., description="Theme color for the presentation.")
):
    url = "https://api.presentationgpt.com/presentations"
    api_key = os.getenv("PRESENTATIONGPT_API_KEY")

    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured.")

    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "userInput": user_input,
        "themeColor": theme_color
    })

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return {
            "status": "success",
            "message": "Presentation generated successfully.",
            "text": response.text
        }

    except Exception as err:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(err)}"
        )
