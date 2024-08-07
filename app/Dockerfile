FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main.server:app", "--host", "0.0.0.0", "--port", "80"]