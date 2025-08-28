from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Author, Book, Genre  # ✅ import all models

engine = create_engine('sqlite:///book_tracker.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

 
Base.metadata.drop_all(engine)
print("Dropping existing tables (if any)...")
 
Base.metadata.create_all(engine)  
print("Creating database tables...")

 
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Fantasy']
for name in genres:
    session.add(Genre(name=name))

try:
    session.commit()
    print("Genres seeded successfully.")
except Exception as e:
    session.rollback()
    print("Error seeding genres:", e)
finally:
    session.close()
