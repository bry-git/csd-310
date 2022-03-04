
--verify user created
SELECT User, Host FROM mysql.user;

-- check permissions on user
SHOW GRANTS FOR whatabook_user;

-- get all data from whatabook
SELECT * FROM user JOIN book JOIN wishlist ON user.user_id = wishlist.user_id AND book.book_id = wishlist.book_id;