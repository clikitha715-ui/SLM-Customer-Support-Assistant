
import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

input_file = BASE_DIR / "data" / "customer_support.json"
data_dir = BASE_DIR / "data"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

random.seed(42)
random.shuffle(data)

total = len(data)

train_end = int(total * 0.70)
validation_end = train_end + int(total * 0.15)

train_data = data[:train_end]
validation_data = data[train_end:validation_end]
test_data = data[validation_end:]

splits = {
    "train.json": train_data,
    "validation.json": validation_data,
    "test.json": test_data
}

for filename, records in splits.items():
    with open(data_dir / filename, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

print("Dataset splitting completed!")
print("Training records:", len(train_data))
print("Validation records:", len(validation_data))
print("Testing records:", len(test_data))
