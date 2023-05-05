
## Set up a Kafka Connector

In this exercise we want to set up an S3 Source connector.
A source connector is one which retreives data from an S3 bucket and produces it into your Kafka cluster.

1. Go to the connectors tab on the left hand side, and search for `Amazon S3 Source`. Click on it.
2. When selecting the type of credentials, you want to provide your connector, choose `Global Access`. Then click on `Generate API key & Download`. Save the keys and click on Continue.
3. For the AWS Credentials:
   Set the AWS access key ID as: `AKIATCJ47SIU54JWJC7G`
   Set the AWS secret access key as: `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`
4. For bucket detail:
   Set S3 bucket name: `confluent-demo-211118166569`
   Set AWS Region: `ap-southest-2`
   Set S3 Path-style Access: No
5. Input mmessage format and output message format, set as JSON for both.
6. The Topic Name Regex Patterns is how we set a topic name and the regex of files we want to read.
   1. For the Regex, set it as `books-slim:.*`
   1. For topics directory, set it as `book-slim/`
7. Set the # of max tasks as 1, it's all we need; then continue.
8. Set a sensible name for your connector

Make a second connector with the same credentials but with following details:
- Regex: `book-prices/`
- Topics directory: `book-prices:.*`