# Create a book stream

Similar to how we created streams in the CLI, we will create one in Confluent.


1. Go to the ksqlDB section via the sidebar
2. When you see a list of ksql Servers, click on your newly created server
3. You should now see the SQL editor on the screen which is equivalent to the CLI
4. Take your previous `CREATE STREAM` statement from the previous lesson and paste it in and click 'Run Query'
5. You should now see the new stream created in the `Streams` tab, it will also appear as a new kafka topic in your cluster.


```sql
CREATE OR REPLACE STREAM book_stream(
    bookID STRING,
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
```