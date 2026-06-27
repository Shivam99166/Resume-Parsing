# 🤖 AI Resume Screener

An AI-powered ATS-inspired Resume Screening Platform that analyzes one or multiple resumes against a job description, generates AI-powered hiring insights, and automatically ranks candidates based on their relevance.

---

# 📌 What It Does

Hiring teams often receive hundreds of resumes for a single job opening. Manually reviewing and comparing every candidate is time-consuming and inconsistent.

AI Resume Screener automates the first stage of recruitment by allowing recruiters to upload one or multiple resumes, compare them against a job description, and receive an AI-generated evaluation.

The platform automatically:

- Uploads one or multiple PDF resumes
- Extracts resume text
- Compares each resume with the job description
- Generates an ATS-style match score
- Detects matching and missing skills
- Provides AI-generated hiring recommendations
- Automatically ranks candidates from best to worst match

This reduces manual screening time and helps recruiters identify the strongest candidates faster.

---

# 🛠 Tech Stack

## Frontend
- React.js
- fetch API
- CSS3
- React Circular Progress Bar

## Backend
- FastAPI
- Python
- Uvicorn

## AI
- Groq API
- Llama 3 8B
- Prompt Engineering

## PDF Processing
- pdfplumber

## Environment
- python-dotenv

## Development Tools
- Git
- GitHub
- VS Code

---

# 🚀 How To Run

## Backend

Clone repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screener.git
```

Move into backend

```bash
cd AI-Resume-Screener/backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Backend

```
http://localhost:3000
```

Swagger Docs

```
http://localhost:8000/docs
```

---

## Frontend

Navigate to frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run application

```bash
npm run dev
```

or

```bash
npm start
```

Frontend

```
http://localhost:5173
```

---

# ✨ Features

### Resume Analysis

- Upload PDF resumes
- Upload multiple resumes simultaneously
- Extract text automatically
- Analyze resumes using AI
- ATS-style candidate evaluation
- AI-powered hiring recommendation
- Match score (0–100)
- Matching skills detection
- Missing skills detection
- Resume summary generation

### Candidate Ranking

- Automatic ranking of multiple candidates
- Best candidate identification
- Side-by-side comparison
- Recruiter-friendly ranking dashboard

### User Experience

- Modern responsive UI
- Circular match score visualization
- Skill badges
- Loading indicators
- FastAPI Swagger documentation

---

# 📂 Project Structure

```
AI-Resume-Screener
│
├── frontend
│   ├── components
│   ├── pages
│   ├── assets
│   └── App.jsx
│
├── backend
│   ├── routes
│   ├── services
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

# 📸 Screenshots


# 🚀 Future Improvements

- Resume preview
- Recruiter authentication
- PostgreSQL database
- Candidate history
- Interview recommendation engine
- Semantic search using vector embeddings
- Resume parsing with OCR for scanned PDFs
- Export analysis reports as PDF
- Docker support
- CI/CD pipeline
- Cloud deployment (Vercel + Render)

---

# 👨‍💻 Author

**Shivam Verma**

- GitHub: https://github.com/Shivam9916
- LinkedIn: https://www.linkedin.com/in/shivam-verma-907823307/
