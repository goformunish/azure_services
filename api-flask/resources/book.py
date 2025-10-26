from flask_restful import Resource
from flask import request
import json

books=[{'id':1,'title': 'java book'},
       {'id':2,'title': 'python book'}]

class BooksGetResource(Resource):
    def get(self):
        return books
    
class BookGetResource(Resource):
    def get(self,id):
        for book in books:
            if book['id']==id:
                return book
        return None
    
class BookPostResource(Resource):
    def put(self,id):
        book=json.loads(request.data)
        new_id=max(book['id'] for book in books)+1
        book['id']=new_id
        books.append(book)
        return book
    
class BookPutResource(Resource):
    def put(self,id):
        book=json.loads(request.data)
        for _book in books:
            if _book['id']==id:
                _book.update(book)
                return _book
            
class BookDeleteResource(Resource):
    def delete(self,id):
        global books
        books=[book for book in books if book['id']!=id]
        return '',204