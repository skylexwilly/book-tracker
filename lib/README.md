 # 📚 Book Tracker

Book Tracker is a simple **command-line application** that helps you manage a collection of **authors, books, and genres** using a relational database.  
It leverages **SQLAlchemy ORM** for database interaction and **Alembic** for database migrations.

---

## ✅ Features

- 📖 Add, list, and delete **Books, Authors, and Genres**  
- ✅ Validated user input to prevent invalid or incomplete entries  
- 🗃️ Uses **SQLAlchemy ORM** for database modeling and querying  
- 🔄 Database schema managed via **Alembic migrations**  

---

## 🏗️ Tech Stack
- Python 3.x  
- SQLAlchemy  
- Alembic  
- SQLite  

---

 🚀 Setup Instructions

 
 
1 .Seed the database with sample data
python -m lib.setup_db

2. Run the CLI application
python -m lib.cli

💻 Usage

When you run the CLI, you’ll see:

📚 Welcome to Book Tracker CLI
Type 'help' to see commands, 'quit' to exit.

Available Commands

authors list → Show all authors

authors add → Add a new author

authors delete → Delete an author

books list → Show all books

books add → Add a new book

genres list → Show all genres

genres add → Add a new genre

quit → Exit the app

📊 Database Schema

Authors

id (PK)

name

Genres

id (PK)

name

Books

id (PK)

title

author_id (FK → Authors.id)

genre_id (FK → Genres.id)

✅ Example Usage
👉 Enter a command: authors list
1: George Orwell
2: Jane Austen
3: J.K. Rowling

👉 Enter a command: books list
1: 1984 (Author: George Orwell, Genre: Fiction)
2: Pride and Prejudice (Author: Jane Austen, Genre: Romance)
3: Harry Potter (Author: J.K. Rowling, Genre: Fantasy)

👉 Enter a command: genres list
1: Fiction
2: Mystery
3: Sci-Fi
4: Fantasy
