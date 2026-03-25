FROM python:3.11-slim

WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python","app.py"]
