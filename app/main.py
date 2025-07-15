import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Reader, Book

# Load env
load_dotenv()

# Create engine
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

# Create tables
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()

# Add a reader
new_reader = Reader(name='Omar', age=19)
session.add(new_reader)
session.flush()

# Add some books
book1 = Book(title='1984', author='George Orwell', genre='Dystopian', owner_id=new_reader.id)
book2 = Book(title='The Hobbit', author='J.R.R. Tolkien', genre='Fantasy', owner_id=new_reader.id)

session.add_all([book1, book2])
session.commit()

# Test
for book in new_reader.books:
    print(f'{new_reader.name} owns {book.title}')

# Close session
session.close()