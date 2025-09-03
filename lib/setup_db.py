 # lib/setup_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Author, Book, Genre

DATABASE_URL = "sqlite:///book_tracker.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def reset_database():
    print("Dropping existing tables (if any)...")
    Base.metadata.drop_all(bind=engine)
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    # Seed Genres
    print("Seeding genres...")
    genres = [
        Genre(name="Fiction"),
        Genre(name="Non-Fiction"),
        Genre(name="Mystery"),
        Genre(name="Sci-Fi"),
        Genre(name="Fantasy"),
    ]
    session.add_all(genres)
    session.commit()

    # Seed Authors
    print("Seeding authors...")
    authors = [
        Author(name="J.K. Rowling"),
        Author(name="George R.R. Martin"),
        Author(name="Agatha Christie"),
        Author(name="Isaac Asimov"),
        Author(name="Yuval Noah Harari"),
    ]
    session.add_all(authors)
    session.commit()

    # Seed Books
    print("Seeding books...")
    books = [
        Book(title="Harry Potter and the Philosopher's Stone", author_id=1, genre_id=5),
        Book(title="A Game of Thrones", author_id=2, genre_id=5),
        Book(title="Murder on the Orient Express", author_id=3, genre_id=3),
        Book(title="Foundation", author_id=4, genre_id=4),
        Book(title="Sapiens: A Brief History of Humankind", author_id=5, genre_id=2),
    ]
    session.add_all(books)
    session.commit()

    print("Database seeded successfully with authors, books, and genres ✅")


if __name__ == "__main__":
    reset_database()
