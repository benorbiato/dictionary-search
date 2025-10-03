# Dictionary Search

**Dictionary Search** is a Python project demonstrating efficient word searches using linear and hash-based methods, along with concurrency and a RESTful API.

## Key Features

* **RESTful API**: FastAPI endpoints to list, search, and add words.
* **Concurrency**: Parallel word search using threads and locks.
* **Performance**: Compare sequential vs concurrent execution times.

## Project Structure

```
dictionary-search/
│
├── data/
│   └── dictionary.json        # Word list in JSON
│
├── src/
│   ├── search.py              # Linear and hash search functions
│   ├── dictionary_loader.py   # Loads dictionary from JSON
│   ├── api_design.py          # FastAPI implementation
│   └── concurrency_demo.py    # Parallel search and performance demo
│
└── requirements.txt           # Dependencies
```

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/your-username/dictionary-search.git
cd dictionary-search
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the API

```bash
uvicorn src.api_design:app --reload
```

* Access API at `http://127.0.0.1:8000`
* Interactive docs: `http://127.0.0.1:8000/docs`

### Run Concurrency Demo

```bash
python src/concurrency_demo.py
```

* Measures execution time for linear vs hash searches, sequential vs concurrent.

## Big O Complexity

| Method        | Time Complexity |
| ------------- | --------------- |
| Linear Search | O(n)            |
| Hash Search   | O(1) average    |
| Adding Word   | O(1)            |
