-- Create a book_stream
CREATE OR REPLACE STREAM book_stream(
    bookID STRING KEY,
    title STRING,
    authors STRING,
    average_rating DOUBLE,
    isbn STRING,
    isbn13 STRING,
    language_code STRING,
    num_pages STRING,
    ratings_count STRING,
    text_reviews_count STRING,
    publication_date STRING,
    publisher STRING
) WITH (
    KAFKA_TOPIC = 'books',
    VALUE_FORMAT = 'JSON'
);

-- List all books with an average_rating more than 4.5
select title, average_rating from book_stream where average_rating > 4.5
