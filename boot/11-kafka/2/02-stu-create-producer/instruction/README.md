# Instruction


## Task
We're working at a book store and we would like to populate our kafka brokers with information about
our books.

Create the target Kafka topic using the `kafka-python` library.

For this exercise, these two docs pages are the most helpful:
* https://kafka-python.readthedocs.io/en/master/apidoc/KafkaAdminClient.html
* https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html

---
### General steps
1. Read in the `books.json` file in Python
   1. Print them out to see if you're reading them in properly, set these values as a bare minimum in your producer
2. Create a [KafkaProducer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html) class and direct it your running Kafka broker by setting the `bootstrap_servers` argument.
   1. ```python
      producer = KafkaProducer(bootstrap_servers=None, acks='all', key_serializer=None, value_serializer=None)
      ```
3. Send the individual rows of books to Kafka hosted by your `docker-compose.yml`
   1. Send the record to the broker with the key as the `bookID`
   2. Send the entire row as the value for that record
   3. Make sure these objects are converted to bytes or to string, which can then be converted to bytes in the key/value deserializers. 
   How can you make this synchronous?
4. Can you see all those records in the Conduktor console under the `books` topic?
 

