FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Ensure Gunicorn is installed
RUN pip3 install gunicorn

# Copy application code
COPY . .

# Expose the application port
EXPOSE 6000

# Start Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:6000", "myproject.wsgi:application"]
