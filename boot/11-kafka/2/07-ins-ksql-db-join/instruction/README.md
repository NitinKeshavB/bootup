# Joining two streaming datasets

We want to join two streaming datasets in this exercise.

---

# General Steps

1. First, we need to load a new dataset called `book_price_stream`.
2. Use the `producer.py` provided to load the book prices into a new Kafka topic.
3. Create a new stream with all the columns as provided. See the previous exercise as a hint on how to do this.
4. Create a new stream called `book_price_deltas` which is a result of a join between `book_stream` stream and `book_price_stream`.
   1. Hint: Use the `CREATE STREAM ... AS SELECT` syntax to make it easier
5. You will be asked to provide a join window, for this purpose, choose `1 MINUTE`. Do you see any results? Try `1 DAY` as well, what do you see?

