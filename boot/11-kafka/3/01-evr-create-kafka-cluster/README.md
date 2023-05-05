# Setting up the pre-requisites on Confluent

We have two small exercises we'd like to do here.
First is the set up a kafka cluster and then we would like to set up a topic.

We want these two items set up in preparating for the next section on connectors. 

## Creating a Kafka Cluster in Confluent Cloud

1. Follow the onboarding to create a new Environment
2. Click into your environment and click on `+ Add Cluster`
3. Choose the `Basic` configuration option
4. For cloud provider and  cluster region, choose AWS and `ap-southest-2` respectively.
   5. Picking the right cloud provider and region is important. Single zone availability is enough.
5. Skip the credit card information, not required. 
6. Give your cluster a name and hit `Launch Cluster`.
7. **You have your first fully managed Kafka cluster!**


## Create a Kafka Topic
1. Go to the topics section on the left side
2. Click on `Create Topic`
3. Name your topic `books`, set partitions to default which is 6.


