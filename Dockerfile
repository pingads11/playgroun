FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD [ "python3", "/app/students-restapi.py", "--host=0.0.0.0"]
