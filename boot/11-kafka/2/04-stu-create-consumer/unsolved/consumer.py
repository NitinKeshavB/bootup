from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json

# Create a producer object
producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                         acks=1,
                         key_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


consumer = KafkaConsumer('books',
                         auto_offset_reset='earliest',              # same as --from-beginning
                         group_id='my-group',
                         enable_auto_commit=False,                  # Bookmarking is disabled
                         bootstrap_servers=['localhost:9092'],
                         key_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Read from the consumer
for message in consumer:
    pass
    # printing out the messages
    #     key = message.key
    #     value = message.value

    # Only keep books with a rating > 4.1

    # Send best books to `best_books` topic.

