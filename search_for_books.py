import pandas as pd
import json
class searchBookDetail:
    def __init__(self, query):
        self.query = query

    def search_books_details(self):
        df = pd.read_csv('books.csv')
        column = list(self.query.keys())[0]
        book_columns = list(df.columns)
        if column in book_columns:
            value = list(self.query.values())[0]
            search_result = json.loads(df[df[column]==value].to_json(orient = 'records'))
            return search_result
        else:
            return 'error'