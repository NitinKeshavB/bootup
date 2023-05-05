# Creating a Kafka Topic

In this exercise we'll be creating a Kafka topic from inside the docker container.

From the last exercise, you should be still inside your docker container.
If not, follow ths instructions in the [previous lesson](../00-evr-setup-env/README.md).

## Creating a Kafka topic
1. Create a kafka topic like so
`kafka-topics --create --topic=messages --bootstrap-server=localhost:9092 --replication-factor=1 --partitions=3`
    * Breakdown of the commands:
        * `--replication-factor`: the number of replicas you want of this topic. The max for this is the number of brokers you have.
        * `--partitions`: the number of partitions you want for the topic. There are guidelines based on your latency, availability and scalability requirements.

1. You can see if it's been created bu running
`kafka-topics --list --bootstrap-server=localhost:9092`
    * You should now be able to see your messages topic there!

