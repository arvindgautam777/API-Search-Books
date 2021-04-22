'''Basic test script to test whether connection is getting established'''
import json
import requests

from flask import json


def test_rows_of_books():
    res = requests.post("http://127.0.0.1:5000/row=2")

    #status code 200 implies successfull response
    assert res.status_code == 200


def test_search_books():
    data = {"authors":"Jesse Grant"}
    r = requests.post("http://127.0.0.1:5000/search", json = data)
	#status code 200 implies successfull response
    assert r.status_code == 200

    #testing for wrong column name
    data2 = {"autho":"Jesse Grant"}
    r = requests.post("http://127.0.0.1:5000/search", json = data2)
    assert r.status_code == 200
    assert r.json() == {'error': 'Column not found'}

