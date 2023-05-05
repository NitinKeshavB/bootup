
-- Create Book Price Stream
CREATE STREAM book_price_stream(
    bookID STRING KEY,
    price_date STRING,
    price DOUBLE
) WITH (
    KAFKA_TOPIC = 'book_prices',
    VALUE_FORMAT = 'JSON'
);

-- Create stream join
CREATE STREAM book_price_change_stream AS
SELECT
     b.bookID as bookID,
     b.title as title,
     p.price_date as price_date,
     p.price as price
FROM book_stream b
INNER JOIN book_price_stream p
    WITHIN 1 HOUR
    ON p.bookID = b.bookID;
