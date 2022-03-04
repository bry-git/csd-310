DROP DATABASE IF EXISTS whatabook;

CREATE DATABASE whatabook;

USE whatabook;

DROP USER IF EXISTS 'whatabook_user'@'%';

CREATE USER 'whatabook_user'@'%' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'%';

CREATE TABLE user
(
    user_id    INT         NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name  VARCHAR(75) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE book
(
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY (book_id)
);

CREATE TABLE wishlist
(
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id     INT NOT NULL,
    book_id     INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_user
        FOREIGN KEY (user_id) REFERENCES user (user_id),
    CONSTRAINT fk_book
        FOREIGN KEY (book_id) REFERENCES book (book_id)
);

CREATE TABLE store
(
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY (store_id)
);
