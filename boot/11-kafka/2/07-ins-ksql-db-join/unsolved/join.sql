
-- Create Book Price Stream
CREATE STREAM book_price_stream(
    ...
) WITH (
    KAFKA_TOPIC = 'book_prices',
    VALUE_FORMAT = 'JSON'
);

-- Create stream join
CREATE STREAM book_price_change_stream AS
SELECT ...
