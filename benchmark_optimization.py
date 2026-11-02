
import json
import time
import psutil
import os
import gc
from pathlib import Path
from transformers import pipeline

BASE_DIR = Path(__file__).resolve().parents[2]

# Load test dataset
with open(BASE_DIR / "data" / "test.json", "r", encoding="utf-8") as file:
    test_data = json.load(file)

# Load FLAN-T5 Small
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

process = psutil.Process(os.getpid())

def benchmark(max_tokens):
    results = []
    latencies = []
    memory_before = process.memory_info().rss / (1024 * 1024)

    for item in test_data:
        prompt = f"""
        You are a helpful customer support assistant.
        Answer politely and clearly.

        Customer question: {item['question']}
        Answer:
        """

        start = time.perf_counter()

        output = generator(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=False,
            num_beams=1
        )

        latency = time.perf_counter() - start
        latencies.append(latency)

        results.append({
            "question": item["question"],
            "answer": output[0]["generated_text"],
            "latency_seconds": round(latency, 3)
        })

    memory_after = process.memory_info().rss / (1024 * 1024)

    return {
        "average_latency_seconds": round(sum(latencies) / len(latencies), 3),
        "memory_before_mb": round(memory_before, 2),
        "memory_after_mb": round(memory_after, 2),
        "responses": results
    }

print("Running baseline benchmark...")
baseline = benchmark(100)

gc.collect()

print("Running optimized benchmark...")
optimized = benchmark(60)

report = {
    "baseline_100_tokens": baseline,
    "optimized_60_tokens": optimized
}

output_file = BASE_DIR / "reports" / "optimization_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("\nOptimization benchmark completed!")
print("Baseline average latency:", baseline["average_latency_seconds"], "seconds")
print("Optimized average latency:", optimized["average_latency_seconds"], "seconds")
print("Results saved in reports/optimization_results.json")
