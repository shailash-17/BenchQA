
from pathlib import Path
import json

from datasets import load_dataset


DATA_DIR = Path("data/benchmark")
OUTPUT_FILE = DATA_DIR / "qasper_sample.jsonl"


def load_qasper():
    """Download and load the QASPER dataset."""
    dataset = load_dataset("allenai/qasper")

    print("Available dataset splits:")
    for split_name, split_data in dataset.items():
        print(f"{split_name}: {len(split_data)} records")

    return dataset


def save_sample(dataset, split_name="train", sample_size=20):
    """Save a small sample for inspection."""
    if split_name not in dataset:
        raise ValueError(
            f"Split '{split_name}' not found. "
            f"Available splits: {list(dataset.keys())}"
        )

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    split = dataset[split_name]
    count = min(sample_size, len(split))

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        for record in split.select(range(count)):
            file.write(
                json.dumps(record, ensure_ascii=False, default=str)
                + "\n"
            )

    print(f"Saved {count} records to {OUTPUT_FILE}")


def main():
    dataset = load_qasper()
    save_sample(dataset)


if __name__ == "__main__":
    main()
