FROM python:3.9 

WORKDIR /src 

COPY /src . 

RUN pip install -r requirements.txt 

ENV PYTHONPATH=/src
ENV source_db_user=postgres
ENV source_db_password=<replace_with_password>
ENV source_db_server_name=<replace_with_server_hostname>
ENV source_db_database_name=dellstore2
ENV target_db_user=postgres
ENV target_db_password=<replace_with_password>
ENV target_db_server_name=<replace_with_server_hostname>
ENV target_db_database_name=dw-dellstore

CMD ["python", "dellstore/pipeline/dellstore_pipeline.py"]
