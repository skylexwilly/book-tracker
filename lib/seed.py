from lib.models import Session, Author, Book, Genre

 
session = Session()

 
genres_list = ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Fantasy"]
genres_objects = []

for name in genres_list:
    genre = Genre(name=name)
    session.add(genre)
    genres_objects.append(genre)

session.commit()   
print("Genres added successfully!")

 
authors_list = ["J.K. Rowling", "George Orwell", "Agatha Christie", "J.R.R. Tolkien"]
authors_objects = []

for name in authors_list:
    author = Author(name=name)
    session.add(author)
    authors_objects.append(author)

session.commit()   
print("Authors added successfully!")

 
books_list = [
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "genre": "Fantasy"},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction"},
    {"title": "Murder on the Orient Express", "author": "Agatha Christie", "genre": "Mystery"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "Animal Farm", "author": "George Orwell", "genre": "Fiction"}
]

for book_data in books_list:
     
    author = next(a for a in authors_objects if a.name == book_data["author"])
     
    genre = next(g for g in genres_objects if g.name == book_data["genre"])
    book = Book(title=book_data["title"], author_id=author.id, genre_id=genre.id)
    session.add(book)

session.commit()
print("Books added successfully!")
