-- Create Stream
create STREAM temprature_stream(
    city STRING KEY,
    temperature DOUBLE
) with (
    KAFKA_TOPIC = 'temperature',
    VALUE_FORMAT = 'JSON'
);

-- What is the hottest temperature each city has experienced?
SELECT city, max(temperature) from temprature_stream group by city emit changes;


-- What is the average temperature of each of these cities?
SELECT city, avg(temperature) from temprature_stream group by city emit changes;


-- Create table
create TABLE temprature(
    city STRING PRIMARY KEY,
    temperature STRING
) with (
    KAFKA_TOPIC = 'temperature',
    VALUE_FORMAT = 'JSON'
);


-- Query all results in temperature table
select * from temprature emit changes;


