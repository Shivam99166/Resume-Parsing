from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.resume import router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "Resume Screener API is running"}

app.include_router(router)




