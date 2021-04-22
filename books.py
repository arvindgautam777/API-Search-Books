import pandas as pd
import json
class booksDetail:
    def __init__(self, row):
        self.row = int(row)
        
    def book_info(self):
        df = pd.read_csv('books.csv')
        res = json.loads(df[:self.row].to_json(orient = 'records'))
        return res




