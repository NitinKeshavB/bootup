from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json
import json_lines

# The key_serializer and value_serializer is required because we need to send data to kafka in
# bytes OR in a type that can be serialized (ASCII, UTF-8, etc).
# We turn it to JSON (encoded in UTF-8) since it's a common message format

producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                         acks=1,
                         key_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Iterating through the json lines file
with open('temperature.json', 'rb') as f:
    for item in json_lines.reader(f):
        future = producer.send(topic='temperature', key=item['city'], value=item)
        result = future.get(timeout=100)

# Closing the file handle
f.close()

