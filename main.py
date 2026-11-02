
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .model.slm_model import generate_response

app = FastAPI(title="SLM Customer Support Assistant")


class CustomerQuery(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=500
    )


@app.get("/")
def home():
    return {
        "message": "SLM Customer Support API is running"
    }


@app.post("/generate")
def generate(query: CustomerQuery):
    try:
        answer = generate_response(query.question)

        return {
            "question": query.question,
            "answer": answer
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to generate a response. Please try again."
        )
