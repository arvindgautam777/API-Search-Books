# API-Search-Books
I have one file with the name books.csv. 
The CSV file contains the general information about the books, like book name, author, year of publication, etc.
Here I developed two API endpoints.
1. Takes the row number as an input and displays respective number of book details rows
2. Takes JSON request with the column name and its value. Filter the data accordingly.

Implementation.
1. Install the required packages
2. I have used the OOP approach.
3. app.py is the main script with the driver code
        - Flask api code is inside app.py
        - used 2 route functions
        - one handles http request with row number as a parameter
        - second handles the http request with json data
5. books.py has the actual logic implementation for 1st API
        - Has the class with the actual logic
        - creates the pandas data frame and returns specific book details based on rows passed
6. search_for_books.py has actual logic for 2nd API
        - Has the class with actual logic
        - pandas dataframe is created and filter condition is applied based on the column name and its value
        - return the desired filtered output
7. run.py has the script to make the JSON request to the API.
8. Postman or curl can also be used to post the JSON request to the API
