
# SLM Customer Support Assistant

## 1. Introduction

The SLM Customer Support Assistant is an AI-based application designed to answer customer queries. It uses the FLAN-T5 Small language model to generate simple and helpful responses.

The application is developed using Python, Hugging Face Transformers and FastAPI.

## 2. Problem Statement

Customers often need quick assistance with order tracking, delivery, payments, cancellations and refunds. Manual customer support can take time.

This project aims to develop a lightweight AI assistant that can respond to common customer support questions.

## 3. Objectives

- Build a customer support assistant using a Small Language Model.
- Compare different Small Language Models.
- Prepare a customer support dataset.
- Adapt model responses using prompt engineering.
- Optimize response generation.
- Evaluate model outputs.
- Deploy the model through FastAPI.

## 4. Models Compared

Three models were considered:

1. FLAN-T5 Small
2. FLAN-T5 Base
3. Microsoft Phi-2

FLAN-T5 Small was selected because it is lightweight and suitable for a basic demonstration.

## 5. Dataset Preparation

A customer support dataset was created with questions and answers related to:

- Order tracking
- Order cancellation
- Returns
- Delivery
- Payments
- Refunds
- Damaged products

The dataset was divided into:

- Training: 70%
- Validation: 10%
- Testing: 20%

The current dataset contains 10 sample records.

## 6. Model Adaptation

Prompt engineering was used to adapt the model for customer support.

The prompt instructs the model to:
- Answer politely.
- Provide simple and clear responses.
- Focus on customer support topics.
- Suggest contacting customer support when information is unavailable.

This is prompt-based adaptation, not weight fine-tuning.

## 7. Model Optimization

The generation settings were optimized by reducing the maximum output length from 100 to 60 tokens and using deterministic generation with one beam.

## 8. Model Evaluation

The baseline and adapted prompts were evaluated using the same held-out test dataset.

Response generation time was recorded for both approaches.

The results were saved in `evaluation_results.json`.

## 9. Deployment

FastAPI was used to deploy the model as a REST API.

The application provides:

- GET `/` – checks whether the API is running.
- POST `/generate` – accepts a customer question and returns an AI-generated answer.

## 10. Technologies Used

- Python
- FLAN-T5 Small
- Hugging Face Transformers
- FastAPI
- Uvicorn
- JSON
- Visual Studio Code

## 11. Conclusion

The project demonstrates how a lightweight language model can be used to build a customer support assistant.

Prompt engineering and generation settings were applied to improve response instructions and control output length. FastAPI provides an interface for accessing the model.

The current implementation is a starter prototype. A larger dataset and further evaluation are needed before real-world use.
## 9. Optimization and Benchmark Results

The model was optimized by reducing the maximum output tokens from 100 to 60. Deterministic generation was used with do_sample=False and num_beams=1.

### Benchmark Comparison

| Metric | Baseline | Optimized |
|---|---:|---:|
| Maximum output tokens | 100 | 60 |
| Average response time | 0.600 seconds | 0.372 seconds |

The optimized configuration reduced average response time by approximately 38%.

### Benchmark Environment
- Model: Google FLAN-T5 Small
- Hardware: CPU
- Test samples: 2
- Results file: reports/optimization_results.json

Note: These results are preliminary because the test dataset contains only two examples. A larger dataset is required for reliable performance measurements.
## 10. Updated Evaluation Results

The model was evaluated using five held-out customer support questions.

| Metric | Baseline | Adapted |
|---|---:|---:|
| Valid responses | 5/5 | 5/5 |
| Average latency | 0.200 seconds | 0.258 seconds |

Both configurations generated non-empty responses for all five test questions.

The adapted prompt had slightly higher average latency than the baseline in this experiment. Therefore, prompt adaptation improved the task-specific instructions but did not demonstrate a speed improvement.

**Limitation:** Response validity checks only whether the generated answer is non-empty. Human review is still required to assess factual correctness and answer quality. The small test dataset also limits the reliability of these findings.