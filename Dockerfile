FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN ls -la

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api_check:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]