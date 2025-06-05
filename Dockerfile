FROM python:3.12.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Mediatheque.wsgi"]
