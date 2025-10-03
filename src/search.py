from dictionary_loader import load_dictionary

dictionary = load_dictionary()

def linear_search(word: str) -> str | None:
    """Linear search for a word in the dictionary."""
    for key, value in dictionary.items():
        if key == word:
            return value
    return None

def hash_search(word: str) -> str | None:
    """Hash search for a word in the dictionary."""
    return dictionary.get(word)