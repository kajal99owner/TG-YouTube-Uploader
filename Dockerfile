FROM python:3.9-slim-buster  # Or a compatible Python image

WORKDIR /app

# Install system dependencies (if any, e.g., ffmpeg) - IMPORTANT!
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg  # Add any needed packages
# Install wget if it's needed for youtube-dl during build, which is unlikely
# RUN apt-get update && apt-get install -y --no-install-recommends wget

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .  # Copy all your bot's code to the /app directory

CMD ["python3", "bot.py"]  # The command to run your bot
