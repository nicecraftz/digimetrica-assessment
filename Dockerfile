FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxcb1 \
    libxkbcommon0 \
    libasound2 \
    libexpat1 \
    libatspi2.0-0 \
    fonts-liberation \
    libappindicator3-1 \
    libcups2 \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install

EXPOSE 8501
ENV PYTHONPATH=/app

CMD ["streamlit", "run", "visualization/streamlit_app.py"]
