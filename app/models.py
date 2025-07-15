from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Create our Base object
Base = declarative_base()

# Create our Reader class
class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    
    books = relationship('Book', back_populates='reader')
    
# Create our Book class
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    genre = Column(String)
    owner_id = Column(Integer, ForeignKey('readers.id'))
    
    reader = relationship('Reader', back_populates='books')