FROM python:3.12.5-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "/app/Livres/manage.py", "runserver", "0.0.0.0:8000"]