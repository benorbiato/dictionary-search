import threading
import time
from time import sleep
from search import linear_search, hash_search, dictionary

# Lock for safe writing
lock = threading.Lock()

# Pythonic dictionary for search methods
search_methods = {
    "hash": hash_search,
    "linear": linear_search
}

# Função de busca
def search_word(word: str, method: str = "hash"):
    """
    Busca uma palavra usando o método especificado
    method: 'hash' ou 'linear'
    """
    search_func = search_methods.get(method, linear_search)
    result = search_func(word)
    print(f"[{threading.current_thread().name}] {method} search: '{word}' => {result}")
    sleep(0.1)  # Simulate processing
    return result

# Concurrent search using threads
def concurrent_search(words: list[str], method: str = "hash"):
    threads = []
    for word in words:
        t = threading.Thread(target=search_word, args=(word, method))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Sequential search
def sequential_search(words: list[str], method: str = "hash"):
    for word in words:
        search_word(word, method)

# Add word safely
def add_word_safe(word: str, definition: str):
    with lock:
        dictionary[word] = definition
        print(f"[{threading.current_thread().name}] Added word: {word}")

if __name__ == "__main__":
    # List of words to search
    words_to_search = list(dictionary.keys())[:20]  # example with 20 words
    method = "hash"

    print("\n=== Sequential Search ===")
    start_seq = time.time()
    sequential_search(words_to_search, method)
    end_seq = time.time()
    print(f"Sequential execution time: {end_seq - start_seq:.4f} seconds\n")

    print("=== Concurrent Search ===")
    start_conc = time.time()
    concurrent_search(words_to_search, method)
    end_conc = time.time()
    print(f"Concurrent execution time: {end_conc - start_conc:.4f} seconds\n")

    # Adding words with threads safely
    new_words = [("orange", "A sweet, orange fruit"), ("pear", "A sweet, green fruit")]
    threads = []
    for word, definition in new_words:
        t = threading.Thread(target=add_word_safe, args=(word, definition))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("All threads finished!")
