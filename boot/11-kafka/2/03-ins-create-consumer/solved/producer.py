from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json
import json_lines

# client = KafkaAdminClient()
# books_topic = NewTopic(name='books', num_partitions=2, replication_factor=1)
# client.create_topics(books_topic)

# The key_serializer and value_serializer is required because we need to send data to kafka in
# bytes OR it has to be serializable.
# We turn it to JSON since it's a common message format

producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                         acks=1,
                         key_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


# Iterating through the json lines file

with open('books.json', 'rb') as f:
    for item in json_lines.reader(f):
        print(item['bookID'])
        # these messages are being processed sychronously since we're waiting for a response
        # and also providing a timeout of 100 millisecnds
        future = producer.send(topic='books', key=item['bookID'], value=item)
        result = future.get(timeout=100)

# Closing the file handle
f.close()

