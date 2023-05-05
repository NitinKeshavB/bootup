FROM python:3.9 

WORKDIR /src 

COPY /src . 

RUN pip install -r requirements.txt 

ENV PYTHONPATH=/src

CMD ["python", "dellstore/pipeline/dellstore_pipeline.py"]
