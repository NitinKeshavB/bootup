FROM python:3.9

WORKDIR /src

ENV API_ENDPOINT="your_api_endpoint" 

COPY /src .

RUN pip install -r requirements.txt 

CMD ["python", "hello_world.py"]
