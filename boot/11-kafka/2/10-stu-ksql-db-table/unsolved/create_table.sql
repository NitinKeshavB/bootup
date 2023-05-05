-- Create Stream
create STREAM temprature_stream(
    ...
) with (
    KAFKA_TOPIC = 'temperature',
    VALUE_FORMAT = 'JSON'
);

-- What is the hottest temperature each city has experienced?


-- What is the average temperature of each of these cities?

-- Create table
create TABLE temprature(
    ...
) with (
    KAFKA_TOPIC = 'temperature',
    VALUE_FORMAT = 'JSON'
);

-- Query all results in temperature table
