# Instruction

## Task
Consume all the records of books from that topic publish just the highest rated books to a new topic called `best_books`.
Create the target Kafka topic using the `kafka-python` library.

For this exercise, these two docs pages are the most helpful:
* https://kafka-python.readthedocs.io/en/master/apidoc/KafkaAdminClient.html
* https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

---
### General steps
1. Create a new file called `consumer.py`
2. Create KafkaConsumer class and direct it towards your running Kafka broker by setting the `bootstrap_servers` argument
3. Consume all the records from the `books` topic you created in the previous exercise
   1. Can you see all the messages coming through? start printing them out as a good first start.
4. Filter out the books to just keep the records with a rating of at least `4.1`
5. Send these best books to a new topic called `best_books` with the key as the `bookID` and the value as
   1. ```json
       {
           "bookID": "45312", 
           "title": "Harry Potter",
           "author": "JK Rowling", 
           "rating": "4.5"
       }
       ```
6. Can you see these records appearing in Conduktor?

