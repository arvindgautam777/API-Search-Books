from flask import Flask, jsonify, request
import requests
from books import booksDetail
from search_for_books import searchBookDetail
app = Flask(__name__)

class get:

	#Below function takes rows as the parameter and return books details
    @app.route('/row=<row>', methods = ['GET', 'POST'])
    def rows_of_books(row):
    	#Creating the object and calling the class
        book_obj = booksDetail(row)
        res = book_obj.book_info()

        #Return the details of the book on the basis of rows
        return jsonify({"books":res})

    @app.route('/search', methods = ['GET', 'POST'])
    def search_books():
        query = request.get_json(force=True)
        print(query)
        search_obj = searchBookDetail(query)
        search_res = search_obj.search_books_details()
        if search_res == 'error':
            return jsonify({"error":"Column not found"})
        else:
            return jsonify({"books":search_res})

if __name__=='__main__':
    app.run(debug = True)