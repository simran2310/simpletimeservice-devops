# Use an official small Python runtime
FROM python:3.11-slim

# Create group & non-root user
RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

WORKDIR /app

# Copy only requirements first for better layer caching
COPY requirements.txt .

# Install dependencies (no dev deps)
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY main.py .

# Expose port and run as non-root user
ENV PORT=8080
EXPOSE 8080

# Switch to non-root user
USER appuser

CMD ["python", "main.py"]
