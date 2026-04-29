USE libraryinventory;

# Stored procedure for task 2 (user story 2)
# After entering a book_id and member_id, a record should be created in loans with all corresponding values and the book should become unavailable in the books table
# An error message will be sent if the chosen book is already unavailable

DELIMITER $$
CREATE PROCEDURE checkout (
	p_book_id INT,
	p_member_id INT
)

BEGIN
	DECLARE available BOOL;
    SELECT is_available INTO available
    FROM books
    WHERE book_id = p_book_id;
    
    IF available = FALSE THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This book is currently unavailable to loan.';
	ELSE
        INSERT INTO loans (book_id, member_id, loan_date) VALUES 
			(p_book_id, p_member_id, CURDATE());
            
        UPDATE books
        SET is_available = FALSE
        WHERE book_id = p_book_id;
            
	END if;
END$$
DELIMITER ;