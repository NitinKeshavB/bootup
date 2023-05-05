FROM python:3.9

WORKDIR /src

ENV API_KEY="my_api_key"
ENV NAME="your_name" 
ENV CITY="your_city"

COPY /src .

RUN pip install -r requirements.txt 

CMD ["python", "hello_world.py"]
