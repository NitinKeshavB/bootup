# Produce messages to Topic

In this lesson, we'd like to produce messages to a kafka topic using the cli.

Opening a Kafka Terminal:
 docker exec -it <container_id> /bin/bash

## Produce a message to a kafka topic
1. Open a new Kafka terminal and open a new producer window like so.
```sh
kafka-console-producer --bootstrap-server localhost:9092 
    --topic messages 
    --property parse.key=true 
    --property key.separator=:
```
What this is saying is that messages need to be written to the kafka topic in the following format
`key:value`
The separator for the ket and value us the `:` character.
For example:
```
key1:message1
```
1. Send a few messages to the `messages` topic by providing a key and a value.
```
key1:message1
key1:message2
key2:message3
key3:message4
```

