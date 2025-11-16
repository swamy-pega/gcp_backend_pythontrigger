#from google import genai
import os
from dotenv import load_dotenv  
from pydantic import BaseModel     
from fastapi import FastAPI, HTTPException,status,Response,Depends,APIRouter
    

from google import genai

load_dotenv()  # Load environment variables from .env file  
key = os.getenv("GEMINI_API_KEY")
#print("GEMINI_API_KEY=", key)

if not key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")


client = genai.Client(api_key=key) 

class Prompt(BaseModel):
    text: str

generate_geminirouter = APIRouter(prefix="/ai/v1" , tags=["generate_text"])

@generate_geminirouter.post("/generate-text")
def generate_gemini(prompt: Prompt):
    try:
        print("Generating text with Gemini API...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt.text
        )
        print("Generated text:", response.text)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}, 500