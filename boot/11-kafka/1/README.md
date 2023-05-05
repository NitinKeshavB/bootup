# Kafka

It's important to remember that this week is about streaming data and that Kafka is just one implementation for streaming data.

## Pre-requisites
* Docker install of Kafka stack
* Download Conduktor
* Have kafka cli installed locally
    * make it easy to setup bootstrap servers

## Starting Kafka

For this course, we will be using Kafka locally.
We will be spinning up Kafka using docker images and orchestrating them using docker compose.

## Breaking down the docker-compose file

* Kafka broker
    * Ports and hostnames (9092 being the default port)
* Zookeeper


## Spin up

* `docker-compose -f zk-single-kafka-single up`

## Exercises
* Create a topic
* List topics
* Creating a topic
* Producing to a topic
* Consuming from a topic
