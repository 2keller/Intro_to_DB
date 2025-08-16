CREATE DATABASE alx_book_store;

USE alx_book_store;
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT REFERENCES authors(author_id),
    price DOUBLE PRECISION NOT NULL,
    publication_date DATE NOT NULL

);

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL

);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT
);
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

);

CREATE TABLE order_details(
    order_id INT REFERENCES orders(order_id),
    book_id INT REFERENCES books(book_id),
    quantity INT NOT NULL
);