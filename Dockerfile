FROM python:3.12.5-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
RUN python -m pip install -r requirements.txt
RUN python /app/Livres/manage.py migrate