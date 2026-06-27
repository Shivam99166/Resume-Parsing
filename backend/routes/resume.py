from fastapi import APIRouter, UploadFile, File, Form
from services.pdf_service import extract_text_from_pdf
from services.groq_service import screen_resume_with_groq
from typing import List
import asyncio

router = APIRouter()

@router.post("/screen-resume")
async def screen_resume(
    files: List[UploadFile] = File(...),
    job_description: str = Form(...)
):
    # Step 1: Read all files and extract text
    texts = []
    filenames = []
    for file in files:
        file_bytes = await file.read()
        text = await extract_text_from_pdf(file_bytes)
        texts.append(text)
        filenames.append(file.filename)

    # Step 2: Process all in parallel
    tasks = [screen_resume_with_groq(t, job_description) for t in texts]
    results = await asyncio.gather(*tasks)

    # Step 3: Add filename and sort by score
    ranked = []
    for i, result in enumerate(results):
        result["filename"] = filenames[i]
        ranked.append(result)

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return {"candidates": ranked}