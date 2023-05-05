#!/bin/bash

# initialise the folder 
octavia init 

# import existing assets 
octavia import all

# list sources available where it is open weather  
octavia list connectors sources | grep openweather 

# create new source and configure YAML 
octavia generate source d8540a80-6120-485d-b7d6-272bca477d9b open_weather_octavia

# list destinations available where it is postgres 
octavia list connectors destinations | grep postgres

# create new destination and configure YAML 
octavia generate destination 25c5221d-dce2-4163-ade9-739ef790f503 dw_octavia 

# run apply to create sources and destinations first 
octavia apply 

# create new connector 
octavia generate connection --source sources/open_weather_octavia/configuration.yaml --destination destinations/dw_octavia/configuration.yaml octavia_example

# run apply to create connector 
octavia apply 

