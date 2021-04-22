import requests

#Using the sample input for 2nd API
data = {"authors":"Jesse Grant"}
#Ensure the app.py is running on the localhost with port:5000
r = requests.post("localhost:5000/search", json = data)
record = r.json()
print(record)
