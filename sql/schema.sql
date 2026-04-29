CREATE SCHEMA IF NOT EXISTS libraryinventory;
USE libraryinventory;

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
	member_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE books (
	book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    is_available BOOL NOT NULL DEFAULT TRUE
);

CREATE TABLE loans (
	loan_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,
    
    CONSTRAINT fk_book_id FOREIGN KEY (book_id) REFERENCES books(book_id),
    CONSTRAINT fk_member_id FOREIGN KEY (member_id) REFERENCES members(member_id)
);