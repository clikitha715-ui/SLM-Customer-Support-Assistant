# Experiment Details

## 1. Model Information
- Model Name: Google FLAN-T5 Small
- Model Identifier: google/flan-t5-small
- Model Type: Small Language Model (SLM)
- Model License: Apache 2.0

## 2. Hardware Environment
- Operating System: Windows
- Programming Language: Python 3.14.7
- Processing Device: CPU
- GPU: Not used

## 3. Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- FastAPI
- Uvicorn
- Pydantic
- Pytest

## 4. Dataset Details
- Dataset: Customer Support Questions and Answers
- Total Examples: 30
- Training Examples: 21
- Validation Examples: 4
- Testing Examples: 5

## 5. Model Adaptation
Prompt engineering was used to adapt the model to customer support tasks. The prompt provides instructions for polite, clear and useful responses.

LoRA, QLoRA and weight fine-tuning were not implemented. Prompt engineering was selected as a lightweight prototype approach because of the limited dataset and CPU environment.

## 6. Optimization Settings
- Baseline Maximum Tokens: 100
- Optimized Maximum Tokens: 60
- Sampling: Disabled
- Beam Count: 1

## 7. Evaluation
- Baseline Average Latency: 0.200 seconds
- Adapted Average Latency: 0.258 seconds
- Baseline Valid Responses: 5/5
- Adapted Valid Responses: 5/5

## 8. Limitations
- Small evaluation dataset.
- No actual model weight fine-tuning.
- Response correctness requires human evaluation.
- CPU-based testing only.