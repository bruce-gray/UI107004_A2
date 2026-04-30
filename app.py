import mysql.connector
from flask import Flask, jsonify

# setup database connection
db = mysql.connector.connect (
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'libraryinventory',
    port = 3306
)

app = Flask(__name__)

# user story 1 - returns the list of available books
@app.route('/books')
def get_books():
    # each endpoint needs a cursor, dictionary = True returns rows as dicts and not tuples (important for jsonify)
    cursor = db.cursor(dictionary=True)
    # executes the query on the database
    cursor.execute('SELECT * FROM books WHERE is_available = TRUE')
    # fetchall retrieves all rows from the query, stores in output
    output = cursor.fetchall()
    # returns contents of output as JSON
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)