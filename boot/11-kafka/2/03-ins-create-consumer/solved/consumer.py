from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json

# Create a producer object
producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                         acks=1,
                         key_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


consumer = KafkaConsumer('books',
                         auto_offset_reset='earliest',
                         group_id='my-group',
                         enable_auto_commit=False,
                         bootstrap_servers=['localhost:9092'],
                         key_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Read from the consumer
for message in consumer:
    # printing out the messages
    print(f"""Key= {message.key}, Value= {message.value}, BookId= {message.value['bookID']}""")

    if float(message.value['average_rating']) > 4.1:
        payload = {
            'bookId': message.value['bookID'],
            'title': message.value['title'],
            'authors': message.value['authors'],
            'rating': message.value['average_rating']}

        # these messages are being processed synchronously since we're waiting for a response
        # and also providing a timeout of 100 milliseconds
        future = producer.send(topic='best_books', key=message.value['bookID'], value=payload)
        result = future.get(timeout=100)


