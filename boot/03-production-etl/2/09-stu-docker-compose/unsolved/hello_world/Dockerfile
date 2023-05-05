FROM python:3.9

WORKDIR /src

ENV API_ENDPOINT="api_endpoint"
ENV NAME="your_name"

COPY /src .

RUN pip install -r requirements.txt 

CMD ["python", "hello_world.py"]
