
import json
from pathlib import Path


FILE_PATH = Path("data/benchmark/qasper_sample.jsonl")


def main():
    if not FILE_PATH.exists():
        print("Dataset sample not found.")
        print("Run: python -m src.corpus.qasper_loader")
        return

    with FILE_PATH.open(encoding="utf-8") as file:
        first_line = file.readline()

    if not first_line:
        print("The dataset sample is empty.")
        return

    record = json.loads(first_line)

    print("\n--- QASPER RECORD STRUCTURE ---")
    for key, value in record.items():
        print(f"{key}: {type(value).__name__}")

    print("\n--- PAPER DETAILS ---")
    print("Title:", record.get("title", "Not available"))
    print("Abstract:", str(record.get("abstract", ""))[:300])

    print("\n--- QUESTIONS AND ANSWERS ---")
    qas = record.get("qas", {})

    if isinstance(qas, dict):
        questions = qas.get("question", [])
        answers = qas.get("answers", [])

        for index, question in enumerate(questions[:3]):
            print(f"\nQuestion {index + 1}: {question}")

            if index < len(answers):
                print("Answer annotation:", answers[index])
    else:
        print("Unexpected QAS structure:", type(qas).__name__)


if __name__ == "__main__":
    main()
