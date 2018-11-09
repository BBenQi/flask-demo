import pymysql
from ..models.book import Book

db = pymysql.connect(host='58.87.111.121', user='root', password='123456', database='wxbook', port=3301)


def get_books(book_name):
    cursor = db.cursor()
    sql = '''SELECT book_name,download_link,book_content FROM book WHERE book_name = '%s'
    ''' % book_name
    cursor.execute(sql)
    books = cursor.fetchall()
    result = []
    for book in books:
        book_model = Book(book[0], book[1], book[2])
        result.append(book_model.__dict__)
    return result
