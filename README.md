# 📚 Library Tracker Flask App

A simple Flask web application that allows users to submit reader and book information through a form, which is stored in a relational database. The app uses SQLAlchemy for ORM functionality and a modular project structure using Blueprints. Planned features include real-time form validation, flash messages, and styled layouts using Flexbox.

---

## 🔗 How to Use

- Clone the repository and install dependencies using `pip install -r requirements.txt`.
- Set up your `.env` file with a `DATABASE_URL` (defaults to SQLite if not provided).
- Run the Flask app (`main.py`) locally.
- Open `http://localhost:5000` in your browser.
- Fill in the reader and book details in the form and click submit.
- The data will be saved to the database.
- Future versions will display saved entries on the homepage and provide instant feedback via flash messages.

---

## 🛠️ Built With

- **Python 3** – Flask framework for routing and app factory structure
- **Flask Blueprints** – For organizing routes
- **SQLAlchemy** – ORM for interacting with the database
- **dotenv** – Load secret keys and database URL from environment variables
- **HTML5 & CSS3** – Form layout and page structure (Flexbox styling coming soon)
- **Flask Flash (planned)** – For user feedback and validation messaging

---

## 📁 Project Features

- Modular Flask app with a clear file structure (`app/`, `main.py`, templates)
- Reader and book submission form saves data to the database
- ORM setup with SQLAlchemy and SQLite/PostgreSQL support
- Environment-based config using `.env` file
- 🚧 **Coming Soon**:
  - Form validation to prevent incomplete or invalid submissions
  - Flash messages to confirm submissions or display errors
  - Display of saved readers and books on the homepage
  - Flexbox-styled layout for a clean, responsive design

---

## 📚 What I Learned

- Structuring a Flask project with app factory pattern and Blueprints
- Setting up SQLAlchemy for persistent data storage
- Managing environment configuration with `dotenv`
- Handling form submission logic and POST requests
- Planning for iterative improvements like validation, UX feedback, and styling

---

## 📫 Connect With Me

- 🌐 [LinkedIn](https://www.linkedin.com/in/omar-jeghalef)
- 📧 [omarjeghalef05@gmail.com](mailto:omarjeghalef05@gmail.com)

---