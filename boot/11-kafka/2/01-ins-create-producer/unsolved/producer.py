from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json
import json_lines


# The key_serializer and value_serializer is required because we need to send data to kafka in
# bytes OR in a type that can be serialized (ASCII, UTF-8, etc).
# We turn it to JSON (encoded in UTF-8) since it's a common message format

# Create a producer

# Iterating through the json lines file
with open('books.json', 'rb') as f:
    for item in json_lines.reader(f):
        print(item)
        # Send records here

# Closing the file handle
f.close()

