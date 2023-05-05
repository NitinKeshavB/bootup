-- Create a book_stream
CREATE OR REPLACE STREAM book_stream(
    ...
) WITH (
    KAFKA_TOPIC = 'books',
    VALUE_FORMAT = 'JSON'
);

-- List all books with an average_rating more than 4.5
SELECT ...
