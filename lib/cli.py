from lib.models import Author, Book, Genre
from lib.db.session import Session


session = Session()

def list_authors():
    authors = session.query(Author).all()
    if not authors:
        print("No authors found.")
        return
    for author in authors:
        print(f"{author.id}: {author.name}")

def add_author():
    name = input("Enter author name: ").strip()
    if name:
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f"Author '{name}' added.")

def delete_author():
    list_authors()
    try:
        author_id = int(input("Enter author ID to delete: "))
        author = session.get(Author, author_id)  # ✅ SQLAlchemy 2.x way
        if author:
            session.delete(author)
            session.commit()
            print(f"Author '{author.name}' deleted.")
        else:
            print("Author not found.")
    except ValueError:
        print("Invalid ID.")

def list_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
        return
    for book in books:
        genre_name = book.genre.name if book.genre else "Unknown"
        author_name = book.author.name if book.author else "Unknown"
        print(f"{book.id}: {book.title} (Author: {author_name}, Genre: {genre_name})")

def add_book():
    title = input("Enter book title: ").strip()
    list_authors()
    author_id = int(input("Enter author ID: "))
    list_genres()
    genre_id = int(input("Enter genre ID: "))

    author = session.get(Author, author_id)
    genre = session.get(Genre, genre_id)

    if author and genre:
        book = Book(title=title, author=author, genre=genre)
        session.add(book)
        session.commit()
        print(f"Book '{title}' added.")
    else:
        print("Invalid author or genre.")

def list_genres():
    genres = session.query(Genre).all()
    if not genres:
        print("No genres found.")
        return
    for genre in genres:
        print(f"{genre.id}: {genre.name}")

def add_genre():
    name = input("Enter genre name: ").strip()
    if name:
        genre = Genre(name=name)
        session.add(genre)
        session.commit()
        print(f"Genre '{name}' added.")

def main():
    print("📚 Welcome to Book Tracker CLI")
    print("Type 'help' to see commands, 'quit' to exit.")

    commands = {
        "authors list": list_authors,
        "authors add": add_author,
        "authors delete": delete_author,
        "books list": list_books,
        "books add": add_book,
        "genres list": list_genres,
        "genres add": add_genre,
    }

    while True:
        cmd = input("\n👉 Enter a command: ").strip().lower()
        if cmd == "quit":
            break
        elif cmd == "help":
            print("\nAvailable commands:")
            for c in commands:
                print(f" - {c}")
        elif cmd in commands:
            commands[cmd]()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
