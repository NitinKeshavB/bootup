# Instruction

## Task 

Create a docker container that prints the following to the console: 

```
Hello World!
It's a wonderful day today
 ____          _     
| __ )   ___  | |__  
|  _ \  / _ \ | '_ \ 
| |_) || (_) || |_) |
|____/  \___/ |_.__/ 
                     

It is currently 14.31 degrees celcius.
```

Think about what library dependencies are required in your `requirements.txt` file to achieve this result. 

The container should be ran using the following parameters: 

```
docker run -e NAME=Bob -e API_KEY=<your_api_key> -e CITY=<your_city> --name <your_container_name> <your_image_name:version>
```

Make use of the [OpenWeather API](https://openweathermap.org/) to get the current weather. 

