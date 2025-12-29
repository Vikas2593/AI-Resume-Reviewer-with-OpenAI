# AI-Powered Resume Review System

An intelligent resume evaluation system built using **LangChain** and **OpenAI GPT models** that analyzes a candidate's resume against a job description and generates a structured, human-readable HTML report.

---

## 🚀 Features

- AI-based resume screening using LLMs
- Skill matching & gap analysis
- Experience evaluation
- Suitability score (0–100)
- Hiring recommendation (StrongHire / Hire / Maybe / Reject)
- Structured output using Pydantic
- HTML report with CSS styling
- Automatic page redirection after evaluation

---

## 🛠️ Tech Stack

- Python 3.10+
- LangChain
- OpenAI (GPT-4o-mini)
- Pydantic
- HTML + CSS
- dotenv

## 📂 Project Structure
<img width="254" height="375" alt="image" src="https://github.com/user-attachments/assets/f5150dcf-c389-41e3-89c9-047ffab696da" />


## ⚙️ Installation & Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Vikas2593/AI-Resume-Reviewer-with-OpenAI.git
cd /AI-Resume-Reviewer-with-OpenAI
```

### 2️⃣ Setup Environment & Run Application
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv\Scripts\activate.ps1   # Mac: venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add OPENAI_API_KEY in the .env file
Create a .env file
Add you own OPENAI_API_KEY =""

# Run the application
python app.py

# Stop server: CTRL + C
# Exit virtual environment
deactivate
```

### 📝 Notes
- Ensure .env contains your OPENAI_API_KEY
- Server must be stopped before running deactivate

### 🧠 How It Works

- User enters resume text and job description
- Prompt is dynamically created using PromptTemplate
- OpenAI LLM evaluates the resume
- Structured output enforced using Pydantic
- HTML report is generated and displayed

### 📊 Evaluation Criteria

- Skill alignment
- Relevant experience
- Programming languages
- Overall suitability

#### Score Range	Recommendation
- 85–100 StrongHire
- 70–84	Hire
- 50–69	Maybe
- <50	Reject
