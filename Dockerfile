FROM python:3.11-slim

# Install system-level dependencies for numpy
RUN apt-get update && apt-get install -y \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy your project files
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

COPY . .

# Command to start your application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]