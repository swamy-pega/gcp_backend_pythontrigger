FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run requires PORT variable
ENV PORT=8080

# Start FastAPI (main.py)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
EXPOSE 8080