import json
from confluent_kafka.cimpl import Producer
import ccloud_lib

# config values 
input_file="github_all_columns.ndjson"
num_messages=-1

def read_file(file, num_messages):
    d = 0
    while d != num_messages:
        with open(file, "r", encoding="utf-8") as data_file:
            for line in data_file:
                doc = json.loads(line)
                d += 1
                yield doc
                if d == num_messages:
                    return
        if num_messages == -1:
            num_messages = d

if __name__ == '__main__':
    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud_lib.read_ccloud_config(config_file)

    # Create Producer instance
    producer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
    producer = Producer(producer_conf)

    # Create topic if needed
    ccloud_lib.create_topic(conf, topic)

    delivered_records = 0

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))
    for doc in read_file(input_file, num_messages):
        producer.produce(topic, key=None, value=json.dumps(doc), on_delivery=acked)
        producer.poll(0)
    producer.flush()
    print("{} messages were produced to topic {}!".format(delivered_records, topic))
