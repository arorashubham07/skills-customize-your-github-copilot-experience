from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Python Journey", "author": "Ada Code"},
    {"id": 2, "title": "API Adventures", "author": "Sam Server"},
]


class Book(BaseModel):
    title: str
    author: str


@app.get("/")
def read_root():
    # TODO: Return a JSON welcome message.
    pass


@app.get("/books")
def get_books():
    # TODO: Return the complete books list.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException(status_code=404).
    pass


@app.post("/books")
def create_book(book: Book):
    # TODO: Create a book with a new ID, add it to books, and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Update the matching book or raise HTTPException(status_code=404).
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the matching book or raise HTTPException(status_code=404).
    pass
