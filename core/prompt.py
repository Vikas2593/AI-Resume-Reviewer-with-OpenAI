from langchain_core.prompts import PromptTemplate

resume_review_prompt = PromptTemplate(  
    input_variables=["resume_text", "job_description"],
    template="""
You are an expert technical recruiter and resume evaluator.

Analyze the candidate's resume against the job description.
Be conservative. Do not hallucinate.

Evaluation criteria:
1. Skill alignment
2. Relevant experience
3. Programming languages
4. Overall suitability

Scoring rules:
- suitability_score: 0–100
- recommendation:
  - 85–100 → StrongHire
  - 70–84  → Hire
  - 50–69  → Maybe
  - <50    → Reject

Resume:
{resume_text}

Job Description:
{job_description}"""
)