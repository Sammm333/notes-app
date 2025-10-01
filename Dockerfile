# Use official Python slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Run with Gunicorn (4 workers, auto‑tuned for CPU)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
