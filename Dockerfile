FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# Install build tools and system dependencies for numpy/scikit-learn
RUN apt-get update && \
    apt-get install -y gcc g++ build-essential python3-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
