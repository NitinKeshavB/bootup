# KSQL DB - Creating a Stream

In this exercise we'll using ksqlDB to do simple transformations on data.

---

# General Steps
1. Open up ksqldb in a new terminal window using the following command:
   1. `docker exec -it ksqldb-cli ksql http://ksqldb-server:8088`

2. Using the existing `books` topic, create a KSQL `stream` called `book_stream`.
   1. Create a [KSQL DB Stream](https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/create-stream/)

3. Check if your stream exists using `show streams` in the `ksqldb-cli` terminal

4. Create a stream of all the book data using all the columns JSON file.
   1. Make all the fields a `STRING` type except the `average_rating` which should be a `DOUBLE` type.

5. Write a query to output all the `title`, `average_rating` of books with an `average_rating` > 4.5

