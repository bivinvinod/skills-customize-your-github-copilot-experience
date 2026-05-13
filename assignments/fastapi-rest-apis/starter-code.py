from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

class BookInDB(Book):
    id: int

books: List[BookInDB] = [
    BookInDB(id=1, title="Python Basics", author="Mergington", year=2025),
    BookInDB(id=2, title="FastAPI Guide", author="Mergington", year=2026),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI book catalog API!"}

@app.get("/books", response_model=List[BookInDB])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=BookInDB)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=BookInDB, status_code=201)
def create_book(book: Book):
    next_id = max((b.id for b in books), default=0) + 1
    new_book = BookInDB(id=next_id, **book.dict())
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=BookInDB)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = BookInDB(id=book_id, **updated_book.dict())
            return books[index]
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")

# To run locally:
# uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
