import os
from groq import Groq
from dotenv import load_dotenv
import json
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=GROQ_API_KEY)

async def screen_resume_with_groq(resume_text: str,job_description:str)->str:
    system_prompt = (
        "You are a highly skilled and experienced resume screening assistant. "
        "Your task is to evaluate resumes against job descriptions and provide a clear assessment of the candidate's suitability for the role. "
        "Please analyze the provided resume and job description, and generate a concise summary highlighting the candidate's strengths, weaknesses, and overall fit for the position. "
        "Your response should be structured in a professional manner, focusing on relevant skills, experience, and qualifications."
        "Return ONLY a valid JSON object. No explanation, no markdown, no extra text."
    ) 

    user_message = f"""
    job_description: {job_description}
    resume_text: {resume_text}
   Instructions:
   - score: number out of 100
- matching_skills: array of strings
- missing_skills: array of strings  
- verdict: "Strong Match" or "Moderate Match" or "Weak Match"
- summary: one sentence assessment
    """
    message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    response =  client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=message,
        max_tokens=1024
    )
    raw = response.choices[0].message.content.strip()
  
    if raw.startswith("```"):
     raw = raw.split("```")[1]
    if raw.startswith("json"):
        raw = raw[4:]

    return json.loads(raw.strip())
  
    