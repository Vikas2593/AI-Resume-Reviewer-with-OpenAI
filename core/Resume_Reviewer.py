from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import Field, BaseModel
from typing import Literal
from dotenv import load_dotenv
from core.prompt import resume_review_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class Resume_Review(BaseModel):

    candidate_name: str = Field(description="Write the name of the candidate")
    city: str = Field(description="Write the city of the candidate")
    total_experience: int = Field(description="Write the total years of experience of candidate")
    languages_known: list[str] = Field(description="Write all the programming language known by the candidate")
    skill_matching: list[str] = Field(description="Write all the matching skills to Job description of the candidate")
    skill_unmatched: list[str] = Field(description="Write all the non matching skills to Job description of the candidate")
    suitability_score: int = Field(description="Write down the overall score of candidate out of 100 based on prompt and skill matched") # 0–100
    short_summary: str = Field(description="Write down the short summary about the candidate eligibility")
    recommendation: Literal["StrongHire", "Hire", "Maybe", "Reject"] = Field(description="Write down the recommendation status based on the score and skills")

structure_model = model.with_structured_output(Resume_Review)

def review_resume(resume_text: str, job_description: str) -> dict:
    prompt = resume_review_prompt.format(
        resume_text=resume_text,
        job_description=job_description
    )

    response = structure_model.invoke(
        [SystemMessage(content=prompt)]
    )

    # Convert Pydantic → dict (Streamlit friendly)
    return response.model_dump()

