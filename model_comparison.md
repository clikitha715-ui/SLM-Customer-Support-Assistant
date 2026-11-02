# SLM Model Comparison

## 1. Models Selected for Comparison

### Model 1: FLAN-T5 Small
- Developer: Google
- Parameters: Approximately 80 million
- Capability: Instruction-following, question answering and text generation.
- License: Apache 2.0
- Context length: Up to 512 input tokens.
- Hardware: Suitable for lower-resource systems.
- Suitability: Good for simple customer support tasks.

### Model 2: FLAN-T5 Base
- Developer: Google
- Parameters: Approximately 250 million
- Capability: Question answering, summarization and text generation.
- License: Apache 2.0
- Context length: Up to 512 input tokens.
- Hardware: Requires more memory than FLAN-T5 Small.
- Suitability: Useful for more complex text-generation tasks.

### Model 3: Microsoft Phi-2
- Developer: Microsoft
- Parameters: 2.7 billion
- Capability: Question answering, language understanding and code generation.
- License: MIT
- Context length: 2048 tokens.
- Hardware: Requires more memory and computing resources.
- Suitability: Useful for more advanced language tasks.

## 2. Model Comparison

| Criteria | FLAN-T5 Small | FLAN-T5 Base | Phi-2 |
|---|---|---|---|
| Model size | 80M | 250M | 2.7B |
| License | Apache 2.0 | Apache 2.0 | MIT |
| Context | 512 tokens | 512 tokens | 2048 tokens |
| Resource needs | Low | Medium | Higher |
| Main strength | Simple instructions | Better capacity | Advanced language tasks |

## 3. Selected Model

Selected Model: Google FLAN-T5 Small.

Reason for Selection:

FLAN-T5 Small is selected because it is lightweight, instruction-tuned and suitable for a basic customer support assistant. It requires fewer computing resources than the other compared models and supports question-answering tasks.

## 4. Conclusion

After comparing three models, FLAN-T5 Small was selected for the customer support application because of its smaller size, instruction-following ability and lower resource requirements.