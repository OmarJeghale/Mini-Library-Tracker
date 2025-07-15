# Handle form routes
from flask import Blueprint, render_template, request, redirect, current_app
from .models import Reader, Book

main = Blueprint('main', __name__)

# Default route
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Get info from user
        name = request.form.get("name")
        age = request.form.get("age")
        title = request.form.get("title")
        author = request.form.get("author")
        genre = request.form.get("genre")
        
        # Save info to db
        new_reader = Reader(name=name, age=int(age))
        current_app.session.add(new_reader)
        current_app.session.flush()
        
        new_book = Book(title=title, author=author, genre=genre, owner_id=new_reader.id)
        current_app.session.add(new_book)
        current_app.session.commit()
        
        return redirect('/')
    
    return render_template('index.html')