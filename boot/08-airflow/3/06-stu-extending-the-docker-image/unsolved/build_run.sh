docker build -t extnded_airflow .

docker run -p 8080:8080 -v /$(pwd):/opt/airflow extended_airflow:latest standalonee