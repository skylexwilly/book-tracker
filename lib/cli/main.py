from lib.db.migrations import session
from lib.models.author import Author
from lib.models.book import Book

def menu():
    while True:
        print("\n📚 Book Tracker CLI")
        print("1. Add Author")
        print("2. View Authors")
        print("3. Add Book")
        print("4. View Books by Author")
        print("5. Delete Author")
        print("6. Delete Book")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter author name: ")
            author = Author(name=name)
            session.add(author)
            session.commit()
            print("✅ Author added!")

        elif choice == "2":
            authors = session.query(Author).all()
            for a in authors:
                print(a)

        elif choice == "3":
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            book = Book(title=title, author_id=author_id)
            session.add(book)
            session.commit()
            print("✅ Book added!")

        elif choice == "4":
            author_id = int(input("Enter author ID: "))
            books = session.query(Book).filter_by(author_id=author_id).all()
            for b in books:
                print(b)

        elif choice == "5":
            author_id = int(input("Enter author ID to delete: "))
            author = session.query(Author).get(author_id)
            if author:
                session.delete(author)
                session.commit()
                print("🗑️ Author deleted!")
            else:
                print("❌ Author not found.")

        elif choice == "6":
            book_id = int(input("Enter book ID to delete: "))
            book = session.query(Book).get(book_id)
            if book:
                session.delete(book)
                session.commit()
                print("🗑️ Book deleted!")
            else:
                print("❌ Book not found.")

        elif choice == "0":
            print("👋 Exiting Book Tracker CLI...")
            break
        else:
            print("❌ Invalid choice")
