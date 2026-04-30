import mysql.connector
from flask import Flask, jsonify, request

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
# http://127.0.0.1:5000/books
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

# user story 2 - calls stored procedure to check out a book
# uses a POST request since this sends data
@app.route('/checkout', methods=['POST'])
def checkout_book():
    cursor = db.cursor(dictionary=True)
    # parse the JSON body of the POST request, extract book_id and member_id
    data = request.get_json()
    book_id = data['book_id']
    member_id = data['member_id']
    # calls my 'checkout' stored procedure. db.commit() is required after any write operations
    try:
        cursor.callproc('checkout', [book_id, member_id])
        db.commit()
        return jsonify({'message': 'Book checked out successfully.'})
    # if the book is unavailable my stored procedure returns an error, convert this into a useful response in JSON
    # HTTP status code 400 means bad request
    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 400

# user story 3 - returns list of current loans
# http://127.0.0.1:5000/books
@app.route('/loans')
def get_loans():
    cursor = db.cursor(dictionary=True)
    # executes the query on the database
    cursor.execute('''
        SELECT b.book_id, b.title, m.member_id, m.full_name, l.loan_date 
        FROM loans l 
        JOIN books b ON b.book_id = l.book_id 
        JOIN members m ON m.member_id = l.member_id 
        WHERE return_date IS NULL;
''')
    # fetchall retrieves all rows from the query, stores in output
    output = cursor.fetchall()
    # returns contents of output as JSON
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)