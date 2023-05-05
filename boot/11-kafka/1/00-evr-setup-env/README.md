# Kafka

It's important to remember that this week is about streaming data and that Kafka is just one implementation for streaming data.

## Pre-requisites
* Docker Desktop is installed
* Docker Compose is installed
* Conduktor installed - add links

**Optional**
* Mac users:
    * `brew install kafka`

--- 

## Starting Kafka

* For this course, we will be using Kafka locally.
* We will be spinning up Kafka using `docker-compose`

### Starting a Kafka cluster

In this lesson, we want to be using the CLI to go through the low level details of operating a Kafka producer and consumer.
In the subsequent lessons we'll be covering the Kafka Python libraries and managed Kafka!

1. `docker-compose -f /path/to/zk-single-kafka-single.yml up`
You will see lots of log output in this step, this is normal.
1. To see the running containers, run `docker ps`
This will take upto two minutes to start, in the meantime, let's look at the docker-compose file.
1. Once `confluentinc/cp-kafka` and `confluentinc/cp-zookeeper` are both running and the log output have stabilised, it means clusters are ready.
1. If we would like to interact with the kafka cluster, we need the kafka CLI (command line interface) or SDK (software development kit).
    * The running Kafka container has the CLI installed

### Jumping inside a docker container
1.  Since the Kafka docker container has the Kafka CLI, we'll make use of it by jumping inside it
    * `docker exec -it <container_id> /bin/bash`
1. Running `kafka-topics --list --bootstrap-server=localhost:9092` should return an empty line (which is just an empty list)