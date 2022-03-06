FROM python:3.8

EXPOSE 8000
WORKDIR /app

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./

CMD uvicorn app.main:app --host=0.0.0.0