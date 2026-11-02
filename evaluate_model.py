
import json
import time
from pathlib import Path
from transformers import pipeline

BASE_DIR = Path(__file__).resolve().parents[2]

# Load test dataset
with open(BASE_DIR / "data" / "test.json", "r", encoding="utf-8") as file:
    test_data = json.load(file)

# Load model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

results = []

for item in test_data:
    question = item["question"]

    # Baseline inference
    baseline_prompt = f"Answer this customer question: {question}"

    start = time.perf_counter()
    baseline_output = generator(
        baseline_prompt,
        max_new_tokens=100,
        do_sample=False,
        num_beams=1
    )
    baseline_time = time.perf_counter() - start

    # Adapted prompt
    adapted_prompt = f"""
    You are a helpful customer support assistant.
    Answer politely and clearly.
    Keep the answer simple and useful.
    If you do not know an answer, suggest contacting customer support.

    Customer Question: {question}
    Answer:
    """

    start = time.perf_counter()
    adapted_output = generator(
        adapted_prompt,
        max_new_tokens=100,
        do_sample=False,
        num_beams=1
    )
    adapted_time = time.perf_counter() - start

    baseline_answer = baseline_output[0]["generated_text"].strip()
    adapted_answer = adapted_output[0]["generated_text"].strip()

    results.append({
        "question": question,
        "expected_answer": item["answer"],
        "baseline_answer": baseline_answer,
        "adapted_answer": adapted_answer,
        "baseline_valid": len(baseline_answer) > 0,
        "adapted_valid": len(adapted_answer) > 0,
        "baseline_time_seconds": round(baseline_time, 3),
        "adapted_time_seconds": round(adapted_time, 3)
    })

# Calculate evaluation summary
total = len(results)

summary = {
    "total_test_questions": total,
    "baseline_valid_responses": sum(r["baseline_valid"] for r in results),
    "adapted_valid_responses": sum(r["adapted_valid"] for r in results),
    "baseline_average_latency": round(
        sum(r["baseline_time_seconds"] for r in results) / total, 3
    ) if total else 0,
    "adapted_average_latency": round(
        sum(r["adapted_time_seconds"] for r in results) / total, 3
    ) if total else 0,
    "note": "Response validity checks non-empty output only. Semantic answer quality requires human review."
}

# Save evaluation results
output_file = BASE_DIR / "reports" / "evaluation_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump({
        "summary": summary,
        "results": results
    }, file, indent=4)

print("Model evaluation completed!")
print("Total test questions:", total)
print("Baseline valid responses:", summary["baseline_valid_responses"])
print("Adapted valid responses:", summary["adapted_valid_responses"])
print("Baseline average latency:", summary["baseline_average_latency"], "seconds")
print("Adapted average latency:", summary["adapted_average_latency"], "seconds")
print("Results saved in reports/evaluation_results.json")
