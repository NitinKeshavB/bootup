FROM python:3.9

WORKDIR /src

COPY /src .

RUN pip install -r requirements.txt 

ENV API_KEY="api_key"
ENV CITY="city"

EXPOSE 5000 

CMD ["python", "app.py"]
