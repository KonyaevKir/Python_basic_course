# Run docker building
# docker build . -t app             docker container collecting

# Run web-app
# docker run -it app                running in local machine only
# docker run -p 8000:8000 -it app   running with external access port 8000

FROM python:3.9-buster

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry install

COPY app.py ./

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0 --port=8000
