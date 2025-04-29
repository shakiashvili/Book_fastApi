from fastapi import FastAPI, HTTPException
from model import Book  
# Might come with an issue and preferable to use .model for testing purposes
from typing import List
import uvicorn


app = FastAPI()

books: List[Book] = [
    Book(id=1, author='Dato', description='Roman', year=2005, status='Public'),
    Book(id=2, author='Gio', description='Poem', year=1993, status='Private'),
    Book(id=3, author='Luka', description='History', year=2021),
    Book(id=4, author='Zuka', description='Trilogy', year=2000)]


@app.get('/books/', response_model=List[Book], description='Getting Books')
async def get_books(status=None):
    filtered = [book for book in books if status is None or book.status == status]
    if status is not None and not filtered:
        raise HTTPException(status_code=404, detail='Not found')
    return filtered


@app.post("/books/", response_model=Book)
async def add_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail='Already Existing')
    books.append(book)
    return book


@app.get('/books/{book_id}', response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book.id == book.id:
            return book
    raise HTTPException(status_code=404, detail='Book not found')


@app.put('/books/{book_id}', response_model=Book)
async def update_book(book_id: int, book_update: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = book_update
            return book_update
    raise HTTPException(status_code=404, detail='Book with Id not found')


@app.delete('/books/{book_id}')
def book_deletion(book_id: int):
    '''
    Delete a book by its ID
    '''
    for book in books:
        if book.id == book_id:
            return books.pop(book_id)
    raise HTTPException(
        status_code=404,
        detail='Book not found')


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)