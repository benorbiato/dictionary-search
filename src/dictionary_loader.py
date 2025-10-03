import json
from pathlib import Path

def load_dictionary(filepath: str = "../data/dictionary.json") -> dict:
    with open(Path(__file__).parent / filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    dictionary = load_dictionary()
    print("Dictionary:")
    for word, definition in dictionary.items():
        print(f"{word}: {definition}")
