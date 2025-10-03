from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dictionary_loader import load_dictionary
from typing import List

app = FastAPI()

class DictionaryItem(BaseModel):
    word: str
    definition: str

dictionary = load_dictionary()

@app.get("/dictionary/{word}")
async def get_dictionary_item(word: str) -> DictionaryItem:
    if word not in dictionary:
        raise HTTPException(status_code=404, detail="Word not found")
    return DictionaryItem(word=word, definition=dictionary[word])

@app.get("/dictionary")
async def get_dictionary() -> list[DictionaryItem]:
    return [DictionaryItem(word=word, definition=definition) for word, definition in dictionary.items()]

@app.post("/dictionary")
async def create_dictionary_item(item: DictionaryItem) -> DictionaryItem:
    if item.word in dictionary:
        raise HTTPException(status_code=400, detail="Word already exists")
    dictionary[item.word] = item.definition
    return item