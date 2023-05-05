# Consume messages from a Topic

## Consuming messages
1. Open a new terminal and docker exec into the container like you've done before.

2. Start a consumer window using this command.
`kafka-console-consumer --bootstrap-server localhost:9092 --topic messages  --property print.key=true --property print.value=true`

3. Produce messages to the topic using what we've done previously like so:
```
key4:Hello, World 5
key5:Hello, World 6
key1:Hello, World 7
key2:Hello, World 8
```
You should see these messages in your consumer window too.

1. Notice how you can't see the earlier messages, if you want to see the now, you need to exit this terminal and run the command below.
`kafka-console-consumer --bootstrap-server localhost:9092 --topic messages  --property print.key=true --property print.value=true  --from-beginning`
The only difference between this command and the previous one is the `--from-beginning` flag. 

## Listing consumer groups
1. Open a new terminal and docker exec into the container like you've done before.

2. To see all the consumers, there should just be one, run this command:
`kafka-consumer-groups --bootstrap-server localhost:9092 --list --state`

3. Get the consumer ID and run this command:
`kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group <consumer-group-id>`
This will list all the partitions that consumer has subscribed to along with the latest offset of the partition, current offset and the lag.

