
from transformers import pipeline

MODEL_NAME = "google/flan-t5-small"

generator = pipeline(
    "text2text-generation",
    model=MODEL_NAME
)

def generate_response(question):
    prompt = f"""
    You are a helpful customer support assistant.

    Instructions:
    - Answer politely.
    - Keep answers simple and clear.
    - Help with orders, delivery, payments and refunds.
    - If you do not know an answer, suggest contacting customer support.

    Customer Question: {question}

    Answer:
    """

    result = generator(
        prompt,
        max_new_tokens=60,
        do_sample=False,
        num_beams=1
    )

    return result[0]["generated_text"]
