# Build the app + Connect to db
import os
from dotenv import load_dotenv
from flask import Flask
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load env
load_dotenv()

# Create engine
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///library.db")
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)

# Create the app
def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'
    app.session = Session()
    
    from .routes import main
    app.register_blueprint(main)
    
    return app