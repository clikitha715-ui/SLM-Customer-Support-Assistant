
# SLM Customer Support Assistant

## Project Overview
An AI-powered customer support assistant built using FLAN-T5 Small and FastAPI. It generates responses to common customer questions about orders, delivery, payments, refunds and returns.

## Technologies Used
- Python
- FLAN-T5 Small
- Hugging Face Transformers
- FastAPI
- Uvicorn
- JSON

## Project Structure
```text
SLM-Customer-Support/
├── configs/
├── data/
│   ├── customer_support.json
│   ├── train.json
│   ├── validation.json
│   └── test.json
├── src/
│   ├── data/
│   ├── model/
│   │   └── slm_model.py
│   ├── evaluation/
│   ├── optimization/
│   ├── api/
│   └── main.py
├── reports/
│   ├── problem_statement.md
│   ├── final_report.md
│   └── evaluation_results.json
├── tests/
└── requirements.txt
```

## Installation

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn src.main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/generate` | Generate a customer support response |

## Model
Google FLAN-T5 Small.

## Adaptation
Prompt engineering is used to guide the model's customer support responses.

## Evaluation
Baseline and adapted prompts are compared using the same test dataset. Response times and generated answers are saved in the reports folder.

## Conclusion
This project demonstrates a lightweight customer support assistant using a Small Language Model and FastAPI.
## Optimization and Performance

The FLAN-T5 Small model was optimized by reducing the maximum output tokens from 100 to 60.

### Benchmark Results

| Metric | Baseline | Optimized |
|---|---:|---:|
| Maximum output tokens | 100 | 60 |
| Average latency | 0.600 seconds | 0.372 seconds |

The optimized configuration achieved approximately 38% lower average response latency in the benchmark.

### Benchmark Details
- Model: Google FLAN-T5 Small
- Hardware: CPU
- Test samples: 2
- Results: `reports/optimization_results.json`

**Limitation:** The benchmark uses only two test examples. More test data is needed for reliable performance evaluation.
## Latest Dataset and Evaluation

### Dataset
- Total examples: 30
- Training: 21
- Validation: 4
- Testing: 5

### Evaluation Results

| Metric | Baseline | Adapted |
|---|---:|---:|
| Valid responses | 5/5 | 5/5 |
| Average latency | 0.200 sec | 0.258 sec |

### Experiment Documentation

Detailed experiment settings and environment information are available in:

`reports/experiment_details.md`

### Testing

Automated API tests were executed successfully.

- Home endpoint: PASSED
- Invalid question: PASSED
- Missing question: PASSED

**Total: 3 tests passed.**