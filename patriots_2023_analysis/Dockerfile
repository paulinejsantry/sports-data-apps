FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

ADD ./* $HOME

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT streamlit run app.py --server.port 8000