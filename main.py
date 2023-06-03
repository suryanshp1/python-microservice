from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wiki_func
from mylib.logic import search_wiki
from mylib.logic import phrases as wiki_phrases


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Keyword to search in wikipedia"""
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""
    result = wiki_func(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""
    result = wiki_phrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
