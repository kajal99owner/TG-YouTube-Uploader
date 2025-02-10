FROM python:3.9-slim-buster

WORKDIR /app

# Install system dependencies (e.g., ffmpeg) - IMPORTANT!
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .  # Copy all your bot's code to the /app directory

CMD ["python3", "bot.py"]
