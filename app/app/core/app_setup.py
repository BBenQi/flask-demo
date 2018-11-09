from ..main import app
from ..dao.books import get_books
from flask import request
import json


@app.route("/")
def hello():
    # This could also be returning an index.html
    return '''Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template), '''


@app.route("/getbook", methods=['POST'])
def get_book():
    book_name = request.form['book']
    result = get_books(book_name)
    return json.dumps(result, ensure_ascii=False)
