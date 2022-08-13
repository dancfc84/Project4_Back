import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/books_db')
secret = os.getenv('SECRET', 'a suitable secret')